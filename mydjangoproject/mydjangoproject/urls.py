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
from myapp1.views import index_page
from myapp1.views import coffe_page
from myapp1.views import post_list
from myapp1.views import index_page_themed
from myapp1.views import logout_wiev
from myapp1.views import post_edit
app_name='myapp1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page,name="index"),
    path('coffee/',coffe_page,name="coffee"),
    path('post/<int:pk>/',post_list,name='post_list'),
    path('<int:pk>/',index_page_themed,name='index_page_themed'),
    path('logout/', logout_wiev, name='logout'),
    path('postedit/<int:pk>',post_edit,name='addpost')
]
