# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
#https://medium.com/@peilee_98185/%E7%94%A8-django-form-%E5%BE%9E%E5%89%8D%E7%AB%AF%E5%82%B3%E8%B3%87%E6%96%99%E5%AD%98%E9%80%B2%E8%B3%87%E6%96%99%E5%BA%AB-c99723e63056
class Post(models.Model):
    post = models.CharField(max_length=500)