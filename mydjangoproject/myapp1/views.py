from django.shortcuts import redirect, render, get_object_or_404
from myapp1.models import Post, Comment, Topic, User_Accaunt, CommentForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


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
            return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes})
        elif action == 'Login':
            if role_id is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                try:
                    user = User_Accaunt.objects.get(login=username, password=password)
                    if user is not None:
                        request.session['role_id'] = user.role_id
                        request.session['username'] = user.username
                        return render(request, 'index.html',
                                      context={'data': all_posts, 'topics': all_themes, 'role_id': user.role_id,'username': user.username})
                    else:
                        return redirect('/')
                except User_Accaunt.DoesNotExist:
                    return redirect('/')
            else:
                return logout_wiev(request)
    else:
        return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes})


def delete_post(request, pk):
    username = request.session.get('username', None)
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')


def edit_post(request, pk):
    username = request.session.get('username', None)
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    all_posts = Post.objects.all()
    username = request.session.get('username', None)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Edit':
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            head = request.POST.get('PostHead')
            content = request.POST.get('PostBudy')
            topik = request.POST.get('pets')
            topic = get_object_or_404(Topic, id=topik)
            Post.objects.filter(id=post.id).update(head=head, content=content, publish_datetime=dt_string, topic=topic, image = "Imaginating ebalo")
            return render(request, 'blog/post_edit.html', context={'data': all_posts, 'topics': all_themes})
        if action == 'AddTopic':
            Name = request.POST.get('NameTopic')
            new_Topic = Topic(name=Name)
            new_Topic.save()
            redirect(request.META.get('HTTP_REFERER', '/') + '?next=' + request.path)
        if action == 'DelTopic':
            topik = request.POST.get('TopicList')
            if topik:
                Topic.objects.get(id=int(topik)).delete()
                return redirect('/')
    return render(request, 'blog/post_edit.html', {'username': username,'post_id': post.id, 'topics': all_themes, 'post_head': post.head, 'post_content' : post.content, 'post_topic' : post.topic.name})


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
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Add':
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            head = request.POST.get('PostHead')
            content = request.POST.get('PostBudy')
            topik = request.POST.get('pets')
            topic = get_object_or_404(Topic, id=topik)
            new_post = Post(head=head, content=content, publish_datetime=dt_string, topic=topic, image = "Imaginating ebalo")
            new_post.save()
            return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes})
    return render(request, 'blog/post_add.html',context={'topics': all_themes})


def role(request):
    role_id = request.session.get('role_id', None)
    return {'role_id': role_id}

def Nickname(request):
    nickname = request.session.get('username',None)
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
                gg =request.session['username'] = user.username
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
    return render(request, 'blog/post_list.html', {'post': post, 'comments': comments, 'form': form,'topics':all_themes})


def index_page_themed(request, pk):
    #тут отсортировать посты по группа (по pk)
    all_posts = Post.objects.filter(topic_id=pk)
    all_themes = Topic.objects.all()

    return render(request, 'index.html', context={'filtrovonae': all_posts, 'data': all_posts, 'topics': all_themes})
