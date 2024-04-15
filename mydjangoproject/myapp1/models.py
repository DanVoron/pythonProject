from django.db import models


class Worker(models.Model): #Создание таблицы
    name = models.CharField(max_length=20,blank=False)
    second_name=models.CharField(max_length=20,blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self): #это для вывода красивого в админ панель
        return f'{self.second_name} {self.name}'


class Posts(models.Model):
    header=models.CharField(max_length=40,blank=False)
    text=models.CharField(max_length=350,blank=False)

    def __str__(self):
        return f'{self.header}'