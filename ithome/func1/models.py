from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# class Item(models.Model):
#     stock = models.IntegerField(default=0)
#     price = models.PositiveIntegerField(default=0)
#     last_modify_date = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     """ track of changes """
#     version = models.IntegerField(default=0)

#http://dokelung-blog.logdown.com/posts/220606-django-notes-5-model-and-database
# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"
        
class Profile(models.Model):
    name     = models.CharField(max_length = 50)
    age      = models.IntegerField()
    tel      = models.CharField(max_length = 30)
    address  = models.CharField(max_length = 100)
    email    = models.EmailField()

    def __unicode__(self):
        return self.name
    
    class Meta(object):
        db_table = "profile"


# class User(models.Model):
#     username = models.CharField(max_length = 30)
#     def __unicode__(self):
#         return self.username

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    class Meta(object):
        db_table = "restaurant"
    
class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField()
    #restaurant = models.ForeignKey(Restaurant)

    class Meta(object):
        db_table = "food"

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='文章類別')
    number = models.IntegerField(default=1,verbose_name='分類數目')
    class Meta(object):
        db_table = "category"

class Topic(models.Model):
    text=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text # 返回儲存在text屬性中的字串

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        return self.text

admin.site.register(Music)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Entry)