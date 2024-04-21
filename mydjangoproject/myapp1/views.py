from django.shortcuts import redirect, render, get_object_or_404
from myapp1.models import Post, Comment, Topic, User_Accaunt
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm
from datetime import datetime


def index_page(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    username = request.session.get('username',None)
    if request.method == 'POST':
        if role_id is None:
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User_Accaunt.objects.get(login=username, password=password)
                if user is not None:
                    print(user.role_id)
                    print(username)
                    request.session['role_id'] = user.role_id
                    request.session['username'] = user.username
                    return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes, 'role_id' : user.role_id, 'username' : user.username })
                else:
                    return redirect('/')
            except User_Accaunt.DoesNotExist:
                return redirect('/')
        else:
            return logout_wiev(request)
    else:
        return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes})



def post_edit(request, pk):
    role_id = request.session.get('role_id', None)
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    return render(request, 'blog/post_edit.html', {'post': post, 'topics': all_themes, 'role_id': role_id})


def logout_wiev(request):
    if request.method == 'POST':
        logout(request)
        # После выхода из системы перенаправляем пользователя на главную страницу
        return HttpResponseRedirect(reverse('index'))
    else:
        # Если запрос не является POST, перенаправляем пользователя на главную страницу
        return HttpResponseRedirect(reverse('index'))

def role(request):
    role_id = request.session.get('role_id', None)
    return {'role_id': role_id}

def coffe_page(request):
    all_posts = Post.objects.all()

    return render(request, 'Coffee.html', context={'data': all_posts})

def post_list(request, pk):
    all_themes = Topic.objects.all()
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            print(dt_string)
            comment = form.save(commit=False)
            comment.post = post
            username = request.session.get('username', None)
            # Предполагаем, что у вас есть способ связать текущего пользователя с экземпляром User_Accaunt
            # Например, вы можете использовать имя пользователя или другой уникальный идентификатор
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
