import os
from django.shortcuts import redirect, render, get_object_or_404
from myapp1.models import Post, Comment, Topic, User_Accaunt, CommentForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from mydjangoproject.settings import MEDIA_URL
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from PIL import Image as PilImage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView



class CommentDeleteView(DeleteView):
    model = Comment
    def get_success_url(self):
        return reverse_lazy('post_list', kwargs={'pk': self.object.post.pk})

def index_page(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    username = request.GET.get('username', None)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Reg':
            name = request.POST.get('Username')
            login = request.POST.get('Login')
            password = request.POST.get('Password')
            new_user = User_Accaunt(username=name, login=login, password=password, role_id=1)
            new_user.save()
            return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes,'MEDIA_URL':MEDIA_URL})
        elif action == 'Login':
            if role_id is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                try:
                    user = User_Accaunt.objects.get(login=username, password=password)
                    if user is not None:
                        request.session['role_id'] = user.role_id
                        request.session['username'] = user.username
                        print(FileSystemStorage)
                        return render(request, 'index.html',
                                      context={'data': all_posts, 'topics': all_themes, 'role_id': user.role_id,
                                               'username': user.username,'MEDIA_URL':MEDIA_URL})
                    else:
                        return redirect('/')
                except User_Accaunt.DoesNotExist:
                    return redirect('/')
            else:
                return logout_wiev(request)
    else:
        return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes,'MEDIA_URL':MEDIA_URL})


def delete_post(request, pk):
    username = request.session.get('username', None)
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def edit_post(request, pk):
    role_id = request.session.get('role_id', None)
    username = request.session.get('username', None)
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    all_posts = Post.objects.all()
    username = request.session.get('username', None)
    if role_id == 2:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'Edit':
                if 'myfile1' in request.FILES:
                    file = request.FILES['myfile1']
                    file = resize_uploaded_image(file, 250, 250)
                    fs = FileSystemStorage()
                    filename = fs.save(file.name, file)
                    file_url = fs.url(filename)
                else:
                    file_url = post.image
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                head = request.POST.get('PostHead')
                content = request.POST.get('PostBudy')
                topik = request.POST.get('pets')
                topic = get_object_or_404(Topic, id=topik)
                Post.objects.filter(id=post.id).update(head=head, content=content, publish_datetime=dt_string, topic=topic,
                                                       image=file_url)
                return redirect('/')
        return render(request, 'blog/post_edit.html',
                      {'username': username, 'post_id': post.id, 'topics': all_themes, 'post_head': post.head,
                       'post_content': post.content, 'post_topic': post.topic.name})
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def logout_wiev(request):
    if request.method == 'POST':
        logout(request)
        # Получаем URL для перенаправления после выхода
        next_url = request.POST.get('next', reverse('index'))
        return HttpResponseRedirect(next_url)
    else:
        # Если запрос не является POST, перенаправляем пользователя на главную страницу
        return HttpResponseRedirect(reverse('index'))


def post_add(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    if role_id == 2:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'Add':
                file = request.FILES['myfile1']
                file = resize_uploaded_image(file, 250, 250)
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                file_url =fs.url(filename)
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                head = request.POST.get('PostHead')
                content = request.POST.get('PostBudy')
                topik = request.POST.get('pets')
                topic = get_object_or_404(Topic, id=topik)
                new_post = Post(head=head, content=content, publish_datetime=dt_string, topic=topic,
                                image=file_url)
                new_post.save()
                return redirect('index')
        return render(request, 'blog/post_add.html', context={'topics': all_themes,'MEDIA_URL':MEDIA_URL})
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def role(request):
    role_id = request.session.get('role_id', None)
    return {'role_id': role_id}


def Nickname(request):
    nickname = request.session.get('username', None)
    return {'username': nickname}


def Userlogin(request):
    role_id = request.session.get('role_id', None)
    if role_id is None:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User_Accaunt.objects.get(login=username, password=password)
            if user is not None:
                request.session['role_id'] = user.role_id
                gg = request.session['username'] = user.username
                return redirect(request.META.get('HTTP_REFERER', '/') + '?next=' + request.path + '&username=' + gg)
            else:
                return redirect('/')
        except User_Accaunt.DoesNotExist:
            return redirect('/')
    else:
        return logout_wiev(request)


def UserReg(request):
    name = request.POST.get('Username')
    login = request.POST.get('Login')
    password = request.POST.get('Password')
    new_user = User_Accaunt(username=name, login=login, password=password, role_id=1)
    new_user.save()
    return redirect(request.META.get('HTTP_REFERER', '/') + '?next=' + request.path + '&username=' + name)


def coffe_page(request):
    all_posts = Post.objects.all()
    return render(request, 'Coffee.html', context={'data': all_posts})


def post_list(request, pk):
    all_themes = Topic.objects.all()
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    form = CommentForm()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Login':
            Userlogin(request)
        elif action == 'Reg':
            UserReg(request)
        elif action == 'AddCom':
            form = CommentForm(request.POST)
            if form.is_valid():
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                print(dt_string)
                comment = form.save(commit=False)
                comment.post = post
                username = request.session.get('username', None)
                user_accaunt = User_Accaunt.objects.get(username=username)
                comment.user = user_accaunt
                comment.publish_datetime = dt_string
                comment.save()
                return redirect('post_list', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_list.html',
                  {'post': post, 'comments': comments, 'form': form, 'topics': all_themes})


def index_page_themed(request, pk):
    #тут отсортировать посты по группа (по pk)
    all_posts = Post.objects.filter(topic_id=pk)
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    username = request.GET.get('username', None)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Reg':
            name = request.POST.get('Username')
            login = request.POST.get('Login')
            password = request.POST.get('Password')
            new_user = User_Accaunt(username=name, login=login, password=password, role_id=1)
            new_user.save()
            return render(request, 'index.html',
                          context={'data': all_posts, 'topics': all_themes, 'MEDIA_URL': MEDIA_URL})
        elif action == 'Login':
            if role_id is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                try:
                    user = User_Accaunt.objects.get(login=username, password=password)
                    if user is not None:
                        request.session['role_id'] = user.role_id
                        request.session['username'] = user.username
                        print(FileSystemStorage)
                        return render(request, 'index.html',
                                      context={'data': all_posts, 'topics': all_themes, 'role_id': user.role_id,
                                               'username': user.username, 'MEDIA_URL': MEDIA_URL})
                    else:
                        return redirect('/')
                except User_Accaunt.DoesNotExist:
                    return redirect('/')
            else:
                return logout_wiev(request)
    return render(request, 'index.html', context={'filtrovonae': all_posts,'themeid':pk, 'data': all_posts, 'topics': all_themes, 'MEDIA_URL':MEDIA_URL})

def theme_edit(request):
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    if role_id == 2:
        if request.method == 'POST':
            action = request.POST.get('action')
            all_themes = Topic.objects.all()
            if action == 'AddTopic':
                Name = request.POST.get('NameTopic')
                new_Topic = Topic(name=Name)
                new_Topic.save()
                redirect(request.META.get('HTTP_REFERER', '/') + '?next=' + request.path)
            if action == 'DelTopic':
                topik = request.POST.get('TopicList')
                if topik:
                    Topic.objects.get(id=int(topik)).delete()
                    redirect(request.META.get('HTTP_REFERER', '/') + '?next=' + request.path)
            if action == 'EditTopic':
                Name = request.POST.get('InpEditTopic')
                topik = request.POST.get('TopicList')
                Topic.objects.filter(id=int(topik)).update(name=Name)
        return render(request, 'blog/theme_edit.html',context={'topics': all_themes})
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def resize_uploaded_image(image, max_width, max_height):
    size = (max_width, max_height)
    if isinstance(image, InMemoryUploadedFile):
        memory_image = BytesIO(image.read())
        pil_image = PilImage.open(memory_image)
        img_format = os.path.splitext(image.name)[1][1:].upper()
        img_format = 'JPEG' if img_format == 'JPG' else img_format

        if pil_image.width > max_width or pil_image.height > max_height:
            pil_image.thumbnail(size)

        new_image = BytesIO()
        pil_image.save(new_image, format=img_format)

        new_image = ContentFile(new_image.getvalue())
        return InMemoryUploadedFile(new_image, None, image.name, image.content_type, None, None)
    return image
