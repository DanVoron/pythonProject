"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp1.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp1.views import CommentDeleteView

app_name='myapp1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page,name="index"),
    path('coffee/',coffe_page,name="coffee"),
    path('post/<int:pk>/',post_list,name='post_list'),
    path('<int:pk>/',index_page_themed,name='index_page_themed'),
    path('logout/', logout_wiev, name='logout'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('postedit/<int:pk>/', edit_post, name='post_edit'),
    path('postadd/',post_add,name='post_add'),
    path('theme_edit/',theme_edit,name='theme_edit'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
