from django.shortcuts import render
from django.http import HttpResponse
from django import template

def index(request):
    return render(request,'index.html')

def member(request):
    return render(request,'member.html')
    
def mycrud(request):
    return render(request,'mycrud.html')
# def login(request):
#    return render(request,'login.html')
def car(request):
    return render(request,'car.html')
    
def testindex(request):
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
    return render(request,'pa_comic.html')
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