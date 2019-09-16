from django.shortcuts import render

# Create your views here.
def login(request):

    uname = request.COOKIES.get('uname','')

    pwd = request.COOKIES.get('upwd','')
#用来获取cookie里的用户名和密码，实现自动填写信息
    context = {'uname': uname,
               'pwd': pwd,
               'error': 0}
    try:
        url = request.META['HTTP_REFERER']
        #获取头部的 来源地址
    except:url = '/'
    response = render(request, 'df_user/login.html', context)
    #将请求的url存入cookie，然后登陆后跳回原来的地方
    # render方法返回httpesponse方法
    response.set_cookie('url', url)
    # 在esponse里写入cookie
    return response
    
def register(request):
    return render(request, 'df_user/register.html')

def login_handle(request):
    # 接收表单数据
    post = request.POST
    uname = post.get('username')
    upwd1 = post.get('pwd')
    # 设置默认值
    remember = post.get('remember', '0')

    # 加密
    s1 = sha1()#创建sha1对象
    s1.update(upwd1.encode('utf8'))#要先编码
    upwd = s1.hexdigest()
    # 验证用户是否正确
    user = User.objects.filter(uname=uname).filter(upwd=upwd).first();

    if user:

        url = request.COOKIES.get('url', '/')  # 第二个参数为默认参数，如果url没有，则条首页
        red = HttpResponseRedirect(url)
        # 如果记住密码则将用户名和密码写入cookies
        if remember == '1':

            red.set_cookie('uname', user.uname)
            red.set_cookie('upwd', upwd1)

        else:
            red.set_cookie('uname', '',max_age=-1)
            red.set_cookie('upwd', '',max_age=-1)
            #也应该写入session，会安全一点
            # request.COOKIES['userinfo']=[user.uname,user.upwd]
            #将uname和id写入session用来保持登录状态
        request.session['username'] = uname
        request.session['uid'] = user.id
        return red

    else:
        #如果没有用户，怎返回错误参数，模板界面，根据错误信息给出提示
        context = {'error': 1,
                   'uname': uname}
        return render(request, 'df_user/login.html', context)

def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')
    # allow = post.get('allow')
    # 判断密码是否相等
    if pwd != cpwd:
        return redirect('/user/register')
    # 密码加密
    # 使用sha1加密
    s1 = sha1()
    # sha1加密前，要先编码为比特
    s1.update(pwd.encode('utf8'))
    pwd = s1.hexdigest()
    # 存入数据库
    user = User()
    user.uname = uname
    user.upwd = pwd
    user.uemil = uemail
    user.save()
    print(user.uname)
    return redirect('/user/login')

def register_exist(request):
    uname = request.GET.get('uname')  # 通过url传参的方式
    count = User.objects.filter(uname=uname).count()
    # print(count)
    # 返回json字典，判断是存在，
    return JsonResponse({'count': count})

def logout(request):
    request.session.flush()  # 清空所有session
    return redirect('/')