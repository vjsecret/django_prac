from django.db import models

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


class User(models.Model):
    username = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.username

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