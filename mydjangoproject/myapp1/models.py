from django.db import models


class Worker(models.Model): #Создание таблицы
    name = models.CharField(max_length=20,blank=False)
    second_name=models.CharField(max_length=20,blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self): #это для вывода красивого в админ панель
        return f'{self.second_name} {self.name}'