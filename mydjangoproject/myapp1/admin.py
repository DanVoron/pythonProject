from django.contrib import admin
from .models import Topic, Role, User_Accaunt, Post, Comment

# Register your models here.
admin.site.register(Topic)
admin.site.register(Role)
admin.site.register(User_Accaunt)
admin.site.register(Post)
admin.site.register(Comment)
