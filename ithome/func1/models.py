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

# class User(models.Model):
#     uname = models.CharField(max_length=20)
#     upwd = models.CharField(max_length=40)
#     uemil = models.CharField(max_length=30)
#     urelname =models.CharField(max_length=20,default='')
#     uadr = models.CharField(max_length=100,default='')
#     uphone = models.CharField(max_length=11,default='')

#这部分主要是，添加一个商品类和分类类，在首页根据分类来列出一些商品，而列出的顺序可以是，时间顺序，点击量，或是价格排序
# class TypeInfo(models.Model):
#     ttitle = models.CharField(max_length=20)
#     isDelete = models.BooleanField(default=False) #使用逻辑删除
#     def __str__(self): #这里是 在admin显示的内容
#         return self.ttitle
# class GoodInfo(models.Model):
#     gtitle = models.CharField(max_length=50)
#     gpic = models.ImageField(upload_to='df_goods') #这个其实存的是路劲，admin中添加时同时上传了文件，需要pillow
#     gprice = models.DecimalField(max_digits=5, decimal_places=2)
#     isDelete = models.BooleanField(default=False)
#     gunit = models.CharField(max_length=20,default='500g')
#     gclick = models.IntegerField()#点击量
#     gintro = models.CharField(max_length=100)#简介
#     gdetial = HTMLField()
#     gtype = models.ForeignKey("TypeInfo") #外键
#     gkucun = models.IntegerField(default=0)  # 库存
# 
# 
#     # gadv = models.BooleanField(default=False)#推荐 广告商品
#     def __str__(self):
#         return self.gtitle
#     class Meta(object):
#         db_table = "goodinfo"

# class Cart(models.Model):
#     user = models.ForeignKey('df_user.User')
#     goods = models.ForeignKey('df_goods.GoodInfo')
#     class Meta(object):
#         db_table = "cart"

    
#admin.site.register(Cart)
admin.site.register(Music)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Entry)