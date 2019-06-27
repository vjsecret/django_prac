"""ithome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from func1 import views
# from func1.views import hello_view
# from func1.views import listone
# from restaurants.views import menu, list_restaurants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.testindex),
    path('index', LoginView.as_view(template_name='index.html'), name="index"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('showinfo/<attr>/', views.showinfo),
    path('car', views.car),
    path('comic', views.comic),
    path('article', views.article),
    path('member/<attr>/', views.member),
    path('member/manager/<attr>/', views.manager),
    path('mycrud', views.mycrud),
    #============================owner model==========================
    # 顯示所有主題
    path('topics/',views.topics,name='topics'),
    # 顯示個別主題
    path('topic/<int:topic_id>/',views.topic,name='topic'), #path('<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # ==================test:==========================
    #path('welcome', views.welcome),
    #path('menu', views.menu),
    #path('list_restaurants', views.list_restaurants),
    #path('comment', views.comment),
    path('listone', views.listone),
    path('hello_view', views.hello_view),
    path('print', views.printPage),
    path('pa_comic/', views.pa_comic),
    path('pa_comic/<data>/', views.pa_comic),#無法與上面同時存在
    path('pa_article', views.pa_article),
    path('face/<int:kind>/', views.face),
    # path(r'^hello/', hello_view),
    #path('face', views.face),
    #re_path('face/(\d{1,2})/', views.face),
    #path(r'^face/(?P<kind>[0-9]', views.face),
]
