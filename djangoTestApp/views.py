from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    # render 是渲染模板
    # 使用render的时候，Django会自动找到INSTALLED_APPS中列出的各个app下的templates中的文件
    # DEBUG=True的时候，Django还可以自动找到各app下static文件夹中的静态文件（js，css，图片等资源），方便开发
    # 这就需要把每个app中的templates文件夹中再建一个app的名称，仅和该app相关的模板放在app/templates/app/目录下面
    # return render(request, 'home.html')
    return render(request, 'index.html')


def add(request, a, b):
    # request.GET 可以看成一个字典，用GET方法传递的值都会保存到其中，
    # 可以用 request.GET.get('key', None)来取值，没有时不报错
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))
    # c = int(a) + int(b)
    # return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add', args=(a, b))
    )


def home(request):
    # string = u"哈哈哈，你是个靠谱的聪明的人"
    # 显示一个字符串变量到网页上
    # return render(request, 'home.html', {'string': string})
    # 基本的for循环和list内容显示
    # TurtorList = ['HTML','CSS',"jquery","Python"]
    # return render(request,'home.html',{'TurtorList':TurtorList})
    # 显示字典中内容
    # info_dict = {'site':u'albertom','content':u'各种好东西'}
    # return render(request,'home.html',{'info_dict':info_dict})
    List = map(str, range(100))  # 一个长度为100的List
    return render(request, 'home.html', {'List': List})


from .forms import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的表单时

        if form.is_valid():  # 如果提交的表单合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
