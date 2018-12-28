from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views import View
from .models import *
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
import datetime
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密_码', widget=forms.PasswordInput())


def index(request):
    back = User.objects.first()
    print(back)
    a = request.user
    if str(a) != 'AnonymousUser':
        return render(request, 'index.html')
    else:
        return redirect('/')


def main(request):
    a = request.user
    if str(a) != 'AnonymousUser':
        cityinfo = {'city': '合肥', 'floor': 9, 'croom': '主机房'}
        wendu = 16
        shidu = 40
        swwendu = 30
        swshidu = 40
        if 18 <= wendu <= 50:
            wstate = '正常'
        else:
            wstate = '异常'

        if 20 <= shidu <= 80:
            sstate = '正常'
        else:
            sstate = '异常'

        context = {
            'cityinfo': cityinfo,
            'wendu': wendu,
            'shidu': shidu,
            'swwendu': swwendu,
            'swshidu': swshidu,
            'wstate': wstate,
            'sstate': sstate,

        }
        return render(request, 'views/main.html',context=context)
    else:
            return redirect('/')


def form(request):
    a = request.user
    if str(a) != 'AnonymousUser':
        time1 = datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')
        time2 = datetime.datetime.now().strptime(time1, '%b-%d-%Y %H:%M:%S')
        print(time1, time2)
        user = request.user.username
        if request.method == 'POST':
            massage = request.POST
            print('info:', massage, massage['router'])
            monitor = MonitorInfo(user=user, time=massage['time'], router=massage['router'],
                                  switch=massage['switch'], server=massage['server'], gateway=massage['gateway'],
                                  ups=massage['ups'], flow=massage['flow'], air=massage['air'],
                                  temperature=massage['temperature'],
                                  humidity=massage['humidity'], remark=massage['remark'])
            monitor.save()
        context = {
            'time': time2,
            'user': user,
        }
        return render(request, 'views/form.html', context=context)
    else:
        return redirect('/')



def user(request):
    user = request.user
    if str(user) != 'AnonymousUser':
        return render(request, 'views/user.html')
    else:
        return redirect('/')
    return  render(request, 'views/user.html',{'user':user})


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #校验是否有数据
            #cleaned_date是字典类型里面是提交成功的数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.all().only('username')
            print(user)
            if username in str(user):
                registAdd = None
            else:
                registAdd = User.objects.create_user(username=username, password=password)
            print(registAdd)
            if registAdd == None:
                return render(request,'login/share.html', {'registAdd': registAdd, 'username': username})

            else:
                return render(request, 'login/share.html', {'registAdd': registAdd})
    else:
        uf= UserForm()

    return render(request, 'login/regist.html', {'uf':uf})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re = auth.authenticate(username=username, password=password)
        if re is not None:
            auth.login(request, re)
            return redirect('/index/', {'user': re})
        else:
            return render(request,'login/login.html',{'login_error':'用户名或者秘密错误'})
    return render(request,'login/login.html')

def loginout(request):
    auth.logout(request)
    return redirect('/')

