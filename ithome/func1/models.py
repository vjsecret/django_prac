from django.db import models

# class Item(models.Model):
#     stock = models.IntegerField(default=0)
#     price = models.PositiveIntegerField(default=0)
#     last_modify_date = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     """ track of changes """
#     version = models.IntegerField(default=0)

# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"