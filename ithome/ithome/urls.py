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
from func1 import views
# from func1.views import hello_view
# from func1.views import listone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.testindex),
    path('index', views.index),
    path('member', views.member),
    path('mycrud', views.mycrud),
    # path('login', views.login),
    path('car', views.car),
    path('listone', views.listone),
    path('hello_view', views.hello_view),
    path('print', views.printPage),
	path('pa_comic', views.pa_comic),
    path('face/<int:kind>/', views.face),

    # path(r'^hello/', hello_view),
    #path('face', views.face),
    #re_path('face/(\d{1,2})/', views.face),
    #path(r'^face/(?P<kind>[0-9]', views.face),
]
