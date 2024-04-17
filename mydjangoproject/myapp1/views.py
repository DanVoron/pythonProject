from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from myapp1.models import Post
from myapp1.models import Topic


def index_page(request):

    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()

    return render(request, 'index.html',context={'data':all_posts,'topics':all_themes})

def coffe_page(request):

    all_posts = Post.objects.all()
    all_themes = Topic.objects.all()

    return render(request, 'Coffee.html', context={'data':all_posts})#контекст для передачи


def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_themes = Topic.objects.all()
    return render(request, 'blog/post_list.html', {'post': post,'topics':all_themes})

def index_page_themed(request,pk):
    #тут отсортировать посты по группа (по pk)
    all_posts = Post.objects.filter(topic_id= pk)
    all_themes = Topic.objects.all()

    return render(request,'index.html', context={'filtrovonae':all_posts,'data':all_posts,'topics':all_themes})