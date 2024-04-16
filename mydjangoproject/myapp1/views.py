from django.shortcuts import render
from myapp1.models import Worker
from django.shortcuts import render, get_object_or_404
from myapp1.models import Posts

def index_page(request):

    # new_worker = Worker(name='Иван', second_name='агаугу',salary=80)
    # new_worker.save()

    # worker_to_change = Worker.objects.get(id=5)
    # worker_to_change.second_name = 'GEGE'
    # worker_to_change.save()

    # Worker.objects.get(id=5).delete

    # all_workers = Worker.objects.all() #выводит все из таблицы

    # workers_filtered = Worker.objects.filter(salary=6000)

    # for i in all_workers:
    #     print(f' {i.second_name}, {i.name}, {i.salary}, {i.id}')

    all_posts = Posts.objects.all()

    return render(request, 'index.html',context={'data':all_posts})

def coffe_page(request):
    # new_post = Posts(header='Amogus2', text='gege')
    # new_post.save()

    all_posts = Posts.objects.all()

    # for i in all_posts:
    #     print(f' {i.header}, {i.text}')

    return render(request, 'Coffee.html', context={'data':all_posts})#контекст для передачи


def post_list(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'blog/post_list.html', {'post': post})