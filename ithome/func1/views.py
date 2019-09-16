from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django import template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from func1.models import Topic, Entry
from func1.forms import TopicForm,EntryForm
import pymysql
import datetime
import json
from django.views.decorators.csrf import csrf_exempt

def formTest(request):
    if request.method == 'POST':
        print("==========fred: showinfo post=============")
        print(request)
        print(request.COOKIES)
        print(request.user)
        print(request.get_host)
        print(request.method)
        print(request.scheme)
        print(request.POST.getlist)
        print(request.content_params)
        print(request.path)
        print(request.path_info)
        v1 = request.POST.getlist('username', '')
        print(v1)
        result_list = request.POST.getlist('key', '')
        result = str(result_list)
        print(result)

        db = pymysql.connect(host="localhost", user="test1", password="123", db="item")
        cursor = db.cursor()
        
        #sql = "DELETE FROM my_student WHERE id = 2"
        #sql = "UPDATE my_class SET id = 4 WHERE id = 5"
        #sql = "UPDATE my_profile SET pname = '改小紅檔案' WHERE pname = '小紅檔案'"
        #cursor.execute(sql)
        #db.commit()
        
        cursor.execute("SELECT * FROM my_student")
        #cursor.execute("SELECT cname FROM my_class WHERE id=(SELECT cid FROM my_student WHERE name = '小明');")
        my_student = cursor.fetchall()

        cursor.execute("SELECT * FROM my_class")
        my_class = cursor.fetchall()
        
        cursor.execute("SELECT * FROM my_profile")
        my_profile = cursor.fetchall()

#         cursor.execute("DROP TABLE IF EXISTS listi")
#         sql = """SELECT * FROM `my_student`,
# )"""
#         try:
#             ww=cursor.execute(sql)
#             print(ww)
#             db.commit()
#             print("add success")
#         except:
#             print("add fail")
#             db.rollback()
        db.close()
    return render(request,'ajaxSample.html',locals())

@login_required
def cart(request):
    uid = request.session.get('uid')
    carts = Cart.objects.filter(user_id=uid)

    context = {'title': '購物車',
               'name': 1,
               'carts': carts}
    return render(request, 'cart.html', context)

@csrf_exempt
def addCar(request):
    if request.method == 'POST':
        print("==========fred: showinfo post=============")
        db = pymysql.connect(host="localhost", user="test1", password="123", db="item")
        # if str== "comic":
        #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
        # else:
        #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
        cursor = db.cursor()
        # 按字典返回 
        # cursor = db.cursor(pymysql.cursors.DictCursor)
        
        print(request.path)
        print(request.path_info)
        print(request.content_params)
        print(request.scheme)
        # listA=request.content_params
        # for ix in range(0,len(listA)):
        #     print(listA[ix])
        print(request.POST)
        var1 = request.POST.getlist('title', '')
        print(var1)
        var2 = request.POST.getlist('price', '')
        print(var2)
        print(type(var2))
        print(var2[0])
        #result = str(result_list)

        cursor.execute("DROP TABLE IF EXISTS listi")
        sql = """CREATE TABLE `listi` (
        `id` int(10) DEFAULT NULL,
        `title` char(20) NOT NULL,
        `price` int(10) DEFAULT NULL
        )"""
        cursor.execute(sql)
        #print("Created table Successfull.")
        # cursor.execute("DROP TABLE IF EXISTS idlisti")
        # sql = """CREATE TABLE `idlisti` (
        # `id` int(10) DEFAULT NULL
        # )"""
        # cursor.execute(sql)
        # cursor.execute("DROP TABLE IF EXISTS titlelisti")
        # sql = """CREATE TABLE `titlelisti` (
        # `title` char(20) NOT NULL
        # )"""
        # cursor.execute(sql)
        # cursor.execute("DROP TABLE IF EXISTS pricelisti")
        # sql = """CREATE TABLE `pricelisti` (
        # `price` int(10) DEFAULT NULL
        # )"""
        # cursor.execute(sql)
        
        listAS=[]
        #list=[1, str(var1), int(var2[0])]
        listAS.append(2)
        listAS.append(str(var1[0]))
        listAS.append(int(var2[0]))
        print(type(int(var2[0])))

        a=3
        #sql = "INSERT INTO listi(ID,TITLE,PRICE) VALUES (1,'"+ listAS[1] +"',' + listAS[2] +')"
        sql = "INSERT INTO listi(ID,TITLE,PRICE) VALUES ( '"+str(listAS[0])+"','" + listAS[1] + "','" + var2[0] + "')"
        #sql = """INSERT INTO listi(ID, TITLE,PRICE) VALUES (1, '酒菜',130)""" 
        try:
            cursor.execute(sql)
            db.commit()
            print("add success")
        except:
            print("add fail")
            db.rollback()
        db.close()

        a = {}
        a["result"] = "post_success"
        #return HttpResponse(json.dumps(a), content_type='application/json')
        return HttpResponseRedirect(reverse('showinfo'))
        #return render(request,'showinfo.html',locals())
@csrf_exempt
def carAjax(request):
    # is_ajax = False
    # if request.is_ajax():
    #     is_ajax = True
    # name_dict = {'twz': 'python and Django',
    #              'abc': 'teach Django', 
    #              'is_ajax': is_ajax}
    # return JsonResponse(name_dict)
    if request.method == 'POST':
        a = {}
        a["result"] = "post_success"
        return HttpResponse(json.dumps(a), content_type='application/json')

#django ajax:
#https://zwindr.blogspot.com/2016/02/django-json-ajax.html
#https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/365618/
def ajaxSample(request):
    #a = range(100)
    # safe 預設為 True => 只能傳 dictionary
    # False => 可傳 dic 以外的物件
    #return JsonResponse(list(a), safe=False)
    #return HttpResponse(json.dumps(list(a)), content_type='application/json')
    db = pymysql.connect(host="localhost", user="test1", password="123", db="article")
    # if str== "comic":
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # else:
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
    cursor = db.cursor()
    # 按字典返回 
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    list=getlist("article", cursor)

    db.close()

    print("==========fred: ajaxSample get=============")
    form = TopicForm()
    return render(request,'ajaxSample.html',locals())

def teststore(request):
    #a = range(100)
    # safe 預設為 True => 只能傳 dictionary
    # False => 可傳 dic 以外的物件
    #return JsonResponse(list(a), safe=False)
    #return HttpResponse(json.dumps(list(a)), content_type='application/json')
    db = pymysql.connect(host="localhost", user="test1", password="123", db="article")
    # if str== "comic":
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # else:
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
    cursor = db.cursor()
    # 按字典返回 
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    list=getlist("article", cursor)

    db.close()

    print("==========fred: teststore get=============")
    return render(request,'teststore.html')

def selecAttr(str):
    Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #str(Now)
    if str== "comic":
        food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'漫畫一好吃'}
        food2 = { 'id':2,'title':'漫畫一蒜泥白肉', 'photoid':4, 'content':'漫畫一人氣推薦'}
        return [food1,food2]
    if str== "article":
        food1 = { 'id':1,'title':'文章一', 'photoid':3, 'content':'文章一好吃'}
        food2 = { 'id':2,'title':'文章一蒜泥白肉', 'photoid':4, 'content':'文章一人氣推薦'}
        return [food1,food2]    

def getlist(str, cursor):
    #print(str)
    if str== "comic":
        # Prepare SQL query to select a record from the table.
        sql = "SELECT * FROM CLIST"
        #\
        #    WHERE INCOME > %d" % (1000)
        #print (sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            data={}
            list=[]
            for row in results:
                #print (row)
                id = row[0]
                title = row[1]
                content = row[2]
                photoid = row[3]
                # Now print fetched result
                #print ("id = %s, title = %s, content = %s, photoid = %s" % (id, title, content, photoid ))
                #data.update({"id":row[0], "title":row[1], "content":row[2], "photoid":row[3]})
                #data.setdefault(zip(['id', 'title', 'content', 'photoid'], row))
                data={"id":row[0], "title":row[1], "content":row[2], "photoid":row[3]}
                list.append(data)
            # print(data)
            # print(list)
            return list
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")
    if str== "article":
        sql = "SELECT * FROM ALIST"
        #\
        #    WHERE INCOME > %d" % (1000)
        #print (sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            data={}
            list=[]
            for row in results:
                #print (row)
                id = row[0]
                title = row[1]
                photoid = row[2]
                price = row[3]
                # Now print fetched result
                #print ("id = %s, title = %s, photoid = %d, price = %d" % (id, title, photoid, price ))
                data={"id":row[0], "title":row[1], "photoid":row[2], "price":row[3]}
                list.append(data)
            return list
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")
    if str== "store":
        try:
            food1 = { 'id':1,'title':'文章一', 'photoid':3, 'content':'文章一好吃'}
            food2 = { 'id':2,'title':'文章一蒜泥白肉', 'photoid':4, 'content':'文章一人氣推薦'}
            return [food1,food2]
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")

def index(request):
    return render(request,'index.html')

# def member(request):
#     return render(request,'member.html')
@login_required
def member(request,attr):
    if attr== "info":
        return render(request,'member.html')
    if attr== "manager":
        return render(request,'manager.html')

# def login(request):
#    return render(request,'login.html')
def logout_view(request):
    logout(request)
    #return redirect(request,'index.html')
    #return HttpResponse(reverse('index'))
    return render(request,'index.html')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = auth.authenticate(username=new_user.username, password=request.POST['password1'])
            # auth.login(request, authenticated_user) #進行登入
            #return HttpResponseRedirect(reverse('learning_logs:index'))
            return render(request,'index.html')

    context = {'form': form}
    return render(request, 'register.html', context)
#@csrf_exempt
def showinfo(request, attr):
    db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # if str== "comic":
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # else:
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
    cursor = db.cursor()
    # 按字典返回 
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    list=getlist(attr, cursor)

    db.close()
    if request.method == 'POST':
        print("==========fred: showinfo post=============")
        print(request.path)
        print(request.path_info)
        print(request.content_params)
        print(request.POST)
        result_list = request.POST.getlist('price', '')
        print(result_list)
        result = str(result_list)
        var1 = request.POST.getlist('title', '')
        print(var1)
        var2 = request.POST.getlist('price', '')
        print(var2)
        print(type(var2))
        print(var2[0])
        

        # form = TopicForm(request.POST)
        # if form.is_valid():
        #     new_topic = form.save(commit=False) # 新增區塊
        #     new_topic.owner = request.user # 新增區塊
        #     new_topic.save() # 新增區塊
        # context = {'form': form}
        #return JsonResponse(list)
        alist = {'title': var1[0], 'price': var2[0]}
        #return HttpResponse(json.dumps(alist), content_type='application/json')
        return render(request,'showinfo.html',locals())
    #if request.method!="POST":
    else:
        print("==========fred: showinfo get=============")
        form = TopicForm()
        return render(request,'showinfo.html',locals())

@login_required
def car(request):
    print("==========fred=============")
    print(request)
    #print(request.headers)
    COOKIES=request.COOKIES
    get_host=request.get_host
    owner=request.user
    scheme=request.scheme
    method=request.method
    post=request.POST
    path=request.path
    path_info=request.path_info
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request,'car.html',locals())

@login_required
def mycrud(request):
    return render(request,'mycrud.html')

@login_required
def manager(request,attr):
    if attr== "info":
        return render(request,'member.html')
    else:
    #if attr== "manager":
        return render(request,'manager.html')

def comic(request):
    list = selecAttr("comic")
    # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
    # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
    # comiclist = [food1,food2]
    return render(request,'comic.html',locals())

# def comic(request, data):
#     print(data)
#     print(type(data))
#     #list = selecAttr(attr)
#     # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
#     # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
#     # comiclist = [food1,food2]
#     # return redirect
#     return render(request,'comic.html',{'abc': "Hello Django "},{locals() } )

def article(request):
    list = selecAttr("article")
    return render(request,'article.html',locals())

def pa_comic(request):
    db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS clist")

    sql = """CREATE TABLE `clist` (
    `id` int(10) DEFAULT NULL,
    `title` char(20) NOT NULL,
    `content` char(20) DEFAULT NULL,
    `photoid` int(11) DEFAULT NULL
    )"""
    cursor.execute(sql)
    print("Created table Successfull.")

    sql = """INSERT INTO clist(ID, TITLE,
    CONTENT, PHOTOID)
    VALUES (1,'漫畫一', '漫畫一好吃', 3)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    
    # 再次插入一条记录
    sql = """INSERT INTO CLIST(ID, TITLE,
    CONTENT, PHOTOID)
    VALUES (2,'漫畫一蒜泥白肉', '漫畫一人氣推薦', 4)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    #print (sql)
    print('Yes, Insert Successfull.')
    db.close()
    return render(request,'pa_comic.html')

def pa_article(request):
    db = pymysql.connect(host="localhost", user="test1", password="123", db="article")

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS aList")
    # Create table as per requirement
    sql = """CREATE TABLE `aList` (
    `id` int(10) DEFAULT NULL,
    `title` char(20) NOT NULL,
    `photoid` int(11) DEFAULT NULL,
    `price` int(10) DEFAULT NULL
    )"""

    cursor.execute(sql)
    print("Created table Successfull.")

    sql = """INSERT INTO aList(ID, TITLE, PHOTOID, PRICE)
    VALUES (1,'番茄炒蛋', 3, 60)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    
    # 再次插入一条记录
    sql = """INSERT INTO aList(ID, TITLE, PHOTOID, PRICE)
    VALUES (2,'蒜泥白肉', 4, 150)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    #print (sql)
    print('Yes, Insert Successfull.')
    db.close()
    # INSERT INTO `alist`(`id`, `title`, `photoid`, `price`) VALUES (1,'番茄炒蛋',3,60);
    # INSERT INTO `alist`(`id`, `title`, `photoid`, `price`) VALUES (2,'蒜泥白肉',4,150);
    return render(request,'pa_article.html')

# def pa_article(request):
#     db = pymysql.connect(host="localhost", user="test1", password="123", db="test")
# 
#     cursor = db.cursor()
#     cursor.execute("DROP TABLE IF EXISTS employee")
#     # Create table as per requirement
#     sql = """CREATE TABLE `employee` (
#     `id` int(10) NOT NULL AUTO_INCREMENT,
#     `first_name` char(20) NOT NULL,
#     `last_name` char(20) DEFAULT NULL,
#     `age` int(11) DEFAULT NULL,
#     `sex` char(1) DEFAULT NULL,
#     `income` float DEFAULT NULL,
#     PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
#     cursor.execute(sql)
#     print("Created table Successfull.")
#     #list=['ks', 'ds', 40, 'M', 8000]
#     #sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('" + list[0] + "','" + list[1] + "', '" + str(list[2]) + "','"+ list[3] +"','" + str(list[4]) + "')"
#     sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#     LAST_NAME, AGE, SEX, INCOME)
#     VALUES ('Mac', 'Su', 20, 'M', 5000)"""
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     
#     # 再次插入一条记录
#     # Prepare SQL query to INSERT a record into the database.
#     sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#     LAST_NAME, AGE, SEX, INCOME)
#     VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     #print (sql)
#     print('Yes, Insert Successfull.')
#     db.close()
#     return render(request,'pa_article.html')

#============================owner model==========================
# 顯示所有主題
@login_required
def topics(request):
    print(request.user)
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #讓 Django 只從資料庫中獲取 owner 屬性為當前使用者的 Topic 物件 #topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', locals())

# 顯示個別主題和它的entries
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user: # 請求主題與現在使用者不符合
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', locals())

@login_required
def new_topic(request):
    #print(request.user)
    if request.method != 'POST':
        form = TopicForm()
    else:
        #if request.user!="NULL":
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #必須判斷不是匿名才能save
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    print(context)
    return render(request, 'new_topic.html', locals())

def new_entry(request, topic_id):
    #topics = Topic.objects.order_by('date_added')    
    #print(topics.id)
    topic = Topic.objects.get(id=topic_id) # 使用topic_id來取得正確主題物件
    #entries = topic.entry_set.order_by('-date_added') #新增:topic底下的entry number+1
    # print(topic)
    # print(topic_id)
    # print(entries)
    
    if request.method != 'POST':
        form = EntryForm()        
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            #print(new_entry)
            new_entry.topic = topic
            #print(new_entry.topic)
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    print(context)
    return render(request, 'new_entry.html', locals())

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # print(entry)
    # print(topic)
    # print(topic.id) #編輯完要回到topic頁，所以需要topic id

    if topic.owner != request.user: #@login_required
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    print(context)
    return render(request, 'edit_entry.html', locals())
#============================start basic and test==========================
# def welcome(request):
#     if 'user_name' in request.GET:
#         return HttpResponse('Welcome!~'+request.GET['user_name'])
#     else:
#         return render_to_response('welcome.html',locals())
# def list_restaurants(request):
#     restaurants = Restaurant.objects.all()
#     return render_to_response('restaurants_list.html',locals())
# def menu(request):
#     if 'id' in request.GET:
#         print(type(request.GET['id']))
#         r = Restaurant.objects.get(id=request.GET['id'])
#         return render_to_response('menu.html',locals())
#     else:
#         return HttpResponseRedirect("/restaurants_list/")
# def comment(request,id):
#     if id:
#         r = Restaurant.objects.get(id=id)
#     else:
#         return HttpResponseRedirect("/restaurants_list/")
#     errors = []
#     if 'ok' in request.POST:
#         user = request.POST['user']
#         content = request.POST['content']
#         email = request.POST['email']
#         date_time = datetime.datetime.now()
#         if not user or not content or not email:
#             errors.append('* 有空白欄位，請不要留空')
#         if '@' not in email:
#             errors.append('*    email格式不正確，請重新輸入')
#         if not errors:
#             Comment.objects.create(user=user, email=email, content=content, 
#             date_time=date_time, restaurant=r)
#             user = ''
#             content = ''
#             email = ''
#     return render_to_response('comments.html',locals())

@login_required
def testindex(request):
    print(type(request.user))
    #print(request.user.is_authenticated())
    #return HttpResponse('歡迎光臨我的網站')
    return render(request,'testindex.html')

def listone(request):
    print("hello web")
    return render(request,'basic.html',locals())
    #return HttpResponse("hello world")

def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })

def face(request, kind):
    print(type(kind))
    return render(request,'face.html', {'kind':kind})

def printPage(request):
    # with open('templates/print.html','r',encoding="utf-8") as reader:
    #         t = template.Template(reader.read())
    #         c = template.Context({ 'name':'s1', 'price':60, 'comment':'deli', 'is_spicy':False })
    #         return HttpResponse(t.render(c))

    food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
    food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
    foods = [food1,food2]
    # return render_to_response('print.html',locals())
    return render(request,'print.html',locals())

def cama(request):
    image = cv2.imread('..\static\images\Desert.jpg',1)
    # cv2.imshow("demo", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cap = cv2.VideoCapture(0)
    # while(True):
    #     ret , frame = cap.read()
    #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('frame',gray)
    #     if cv2.waitKey(1) & 0xFF ==ord('q'):
    #     break
    # cap.release()
    # cv2.destroyAllWindows()

def testurl(request, attr):
    #article(request)
    #return redirect
    #print(type(attr))
    #print(type(abc)
    list = selecAttr(attr)
    return render(request,'testurl.html',locals())