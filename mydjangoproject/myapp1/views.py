from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from myapp1.models import Post
from myapp1.models import Topic, User_Accaunt


def index_page(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User_Accaunt.objects.get(login=username, password=password)
            if user is not None:
                print(user.role_id)
                request.session['role_id'] = user.role_id
                return render(request, 'Coffee.html', context={'data': all_posts, 'topics': all_themes})
            else:
                print("Somsyng BAD IDI NAHUI NOOB")
                return redirect('/')
        except User_Accaunt.DoesNotExist:
            return redirect('/')
    else:
        return render(request, 'index.html', context={'data': all_posts, 'topics': all_themes})

def role(request):
    role_id = request.session.get('role_id', None)
    return {'role_id': role_id}


def coffe_page(request):
    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()

    return render(request, 'Coffee.html', context={'data': all_posts})


def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    return render(request, 'blog/post_list.html', {'post': post, 'topics': all_themes})


def index_page_themed(request, pk):
    #тут отсортировать посты по группа (по pk)
    all_posts = Post.objects.filter(topic_id=pk)
    all_themes = Topic.objects.all()

    return render(request, 'index.html', context={'filtrovonae': all_posts, 'data': all_posts, 'topics': all_themes})
