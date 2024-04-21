from django.db import models
from django import forms
class Topic(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'topic'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'role'

    def __str__(self):
        return self.name


class User_Accaunt(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_account'

    def __str__(self):
        return self.username


class Post(models.Model):
    head = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    publish_datetime = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'post'

    def __str__(self):
        return self.head


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User_Accaunt, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    publish_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __str__(self):
        return self.content
