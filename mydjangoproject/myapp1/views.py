from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from myapp1.models import Post
from myapp1.models import Topic, User_Accaunt
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def index_page(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()
    role_id = request.session.get('role_id', None)
    if request.method == 'POST':
        if role_id is None:
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User_Accaunt.objects.get(login=username, password=password)
                if user is not None:
                    print(user.role_id)
                    request.session['role_id'] = user.role_id
                    return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes, 'urmom' : user.role_id })
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
    role_id = request.session.get('role_id', None)
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    return render(request, 'blog/post_list.html', {'post': post, 'topics': all_themes, 'role_id': role_id})


def index_page_themed(request, pk):
    #тут отсортировать посты по группа (по pk)
    all_posts = Post.objects.filter(topic_id=pk)
    all_themes = Topic.objects.all()

    return render(request, 'index.html', context={'filtrovonae': all_posts, 'data': all_posts, 'topics': all_themes})
