from django.shortcuts import render
from myapp1.models import Worker

def index_page(request):

    # new_worker = Worker(name='Иван', second_name='агаугу',salary=80)
    # new_worker.save()

    worker_to_change = Worker.objects.get(id=5)
    worker_to_change.second_name = 'GEGE'
    worker_to_change.save()

    # Worker.objects.get(id=5).delete

    all_workers = Worker.objects.all() #выводит все из таблицы

    workers_filtered = Worker.objects.filter(salary=6000)

    for i in all_workers:
        print(f' {i.second_name}, {i.name}, {i.salary}, {i.id}')

    return render(request, 'index.html')

def coffe_page(request):
    return render(request, 'Coffee.html')