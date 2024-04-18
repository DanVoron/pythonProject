from django.db import models

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'topic'

    def str(self):
        return self.name

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'role'

    def str(self):
        return self.name

class User_Accaunt(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=30)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_account'

    def str(self):
        return self.username

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    publish_datetime = models.DateTimeField()
    topic_id = models.IntegerField()
    image = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'post'

    def str(self):
        return self.head

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.CharField(max_length=250)
    publish_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'

    def str(self):
        return self.content