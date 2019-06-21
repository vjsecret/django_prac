from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
import pymysql
import datetime

def selecAttr(str):
    Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #str(Now)
    if str== "comic":
        db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
        cursor = db.cursor()
        # 按字典返回 
        # cursor = db.cursor(pymysql.cursors.DictCursor)
        getlist("comic")
        db.close()
        food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'漫畫一好吃'}
        food2 = { 'id':2,'title':'漫畫一蒜泥白肉', 'photoid':4, 'content':'漫畫一人氣推薦'}
        return [food1,food2]
    if str== "article":
        food1 = { 'id':1,'title':'文章一', 'photoid':3, 'content':'文章一好吃'}
        food2 = { 'id':2,'title':'文章一蒜泥白肉', 'photoid':4, 'content':'文章一人氣推薦'}
        return [food1,food2]    

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

@login_required
def manager(request,attr):
    if attr== "info":
        return render(request,'member.html')
    else:
    #if attr== "manager":
        return render(request,'manager.html')

@login_required
def mycrud(request):
    return render(request,'mycrud.html')

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

@login_required
def car(request):
    return render(request,'car.html')

@login_required
def testindex(request):
    print(type(request.user))
    #print(request.user.is_authenticated())
    #return HttpResponse('歡迎光臨我的網站')
    return render(request,'testindex.html')

# Create your views here.
def listone(request):
    print("hello web")
    return render(request,'basic.html',locals())
    #return HttpResponse("hello world")

# Create your views here.
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
    db = pymysql.connect(host="localhost", user="test1", password="123", db="test")

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS employee")
    # Create table as per requirement
    sql = """CREATE TABLE `employee` (
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `first_name` char(20) NOT NULL,
    `last_name` char(20) DEFAULT NULL,
    `age` int(11) DEFAULT NULL,
    `sex` char(1) DEFAULT NULL,
    `income` float DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    cursor.execute(sql)
    print("Created table Successfull.")
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Mac', 'Su', 20, 'M', 5000)"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    
    # 再次插入一条记录
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    #print (sql)
    print('Yes, Insert Successfull.')
    db.close()
    return render(request,'pa_article.html')
def getlist(str):
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
            for row in results:
                #print (row)
                id = row[0]
                title = row[1]
                content = row[2]
                photoid = row[3]
                # Now print fetched result
                print ("id = %s, title = %s, content = %s, photoid = %s" % \
                        (id, title, content, photoid ))
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")

def comic(request):
    list = selecAttr("comic")
    # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
    # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
    # comiclist = [food1,food2]
    return render(request,'comic.html',locals())

def comic(request, data):
    print(data)
    print(type(data))
    #list = selecAttr(attr)
    # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
    # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
    # comiclist = [food1,food2]
    # return redirect
    return render(request,'comic.html',{'abc': "Hello Django "},{locals() } )

def article(request):
    list = selecAttr("article")
    return render(request,'article.html',locals())

def testurl(request, attr):
    #article(request)
    #return redirect
    #print(type(attr))
    #print(type(abc)
    list = selecAttr(attr)
    return render(request,'testurl.html',locals())
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