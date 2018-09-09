# coding:utf-8
from django.shortcuts import render,render_to_response
import os
import commands
from django.http import HttpResponse,HttpResponseRedirect
from .models import monitors,User,question,Experience
from django import forms
from django.template import RequestContext
from django.contrib import auth

from cmdb.models  import Information

from webssh.forms import websshform

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
             registusername = User.objects.filter(username=username).get().username
             registered="已经注册了"
             return render(request,'register.html',{'registusername':registusername,'registered':registered})
        except:
            registAdd = User.objects.create(username=username,password=password)
            Registered="注册成功!!!"
            return render(request,'register.html',{'registAdd':registAdd,'Registered':Registered})
    else:
        return render(request,'register.html')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = User.objects.filter(username__exact = username,password__exact = password)
        if user:                                           #如果用户匹配成功
            response = HttpResponseRedirect('/index/')              #重定向到index
            response.set_cookie('cookie_username',username,36)    #设置cookie 
            return response                                         #把index页面输出   
        else:
            nopass="用户名或者密码输入错误"                        #没有匹配成功  
            return render(request,'login.html',{'nopass':nopass}) 
        return HttpResponse('yes')
    return render(request,'login.html')                               




def servers(request):
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")    
        model = request.POST.get("model","")    
        user = request.POST.get("user","")    
        command = request.POST.get("command","") 
        os.environ['hostgroup']=str(hostgroup)
        os.environ['model']=str(model)
        os.environ['user']=str(user)
        os.environ['command']=str(command)
        output = commands.getoutput("sh /home/zqxt_form2/monitor/ansible.sh $hostgroup $model $user $command")
        return render(request,'servers.html',{'output':output})
    return render(request,'servers.html')



def filersync(request):
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")
        srcname = request.POST.get("srcname","")
        destname = request.POST.get("destname","")
        os.environ['hostgroup']=str(hostgroup)
        os.environ['srcname']=str(srcname)
        os.environ['destname']=str(destname)
        output = commands.getoutput("sh /home/zqxt_form2/monitor/filersync.sh $hostgroup   $srcname  $destname")
        return render(request,'filersync.html',{'output':output})
    return render(request,'filersync.html')



def program(request):
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")
        service = request.POST.get("service","")
        status = request.POST.get("status","")
        os.environ['hostgroup']=str(hostgroup)
        os.environ['service']=str(service)
        os.environ['status']=str(status)
        output = commands.getoutput("sh /home/zqxt_form2/monitor/program.sh $hostgroup $service $status ")
        return render(request,'program.html',{'output':output})
    return render(request,'program.html')



def monitorset(request):
    if request.method == 'POST':
        servername =  request.POST.get("servername","")
        item =  request.POST.get("item","")
        value =  request.POST.get("value","")
        serverip  =  request.POST.get("serverip","")
        time = commands.getoutput("date")
        try:
             host = monitors.objects.filter(servername=servername,item=item).get().servername
             return HttpResponse('已经有这个监控项了')
        except:
            monitors.objects.create(servername=servername,item=item,value=value,serverip=serverip,time=time)
            return HttpResponse('创建了这个监控项') 

    return render(request,'monitorset.html')




def deluser(request):
    username = request.COOKIES.get('cookie_username','')
    delusers =  User.objects.filter(username__exact = username).delete()
    deltxt = str(username)+"被删除成功"
    return render(request,'login.html',{'deltxt':deltxt})


#def index(req):
#    username = req.COOKIES.get('cookie_username','')                    #得到cookie_username对应的用户 
#    return render_to_response('index.html',{'username':username})       #针对登录的用户展示欢迎界面

def logout(request):
    return render(request,'login.html')
    response.delete_cookie('cookie_username')                            #删除cookie_username对应的用户的cookie 
    return  response


def index(request):
    date=commands.getoutput('date')
    area=commands.getoutput('sh /home/zqxt_form2/monitor/ip.sh 2>/dev/null ')
    weather=commands.getoutput('python  /home/zqxt_form2/monitor/weather.py  ')
    username = request.COOKIES.get('cookie_username','')
    if  username: 
        return render_to_response('index.html',{'date': date,'area': area,'weather':weather,'username':username})
    else:
        return render(request,'login.html')


def Questions(request):
    date=commands.getoutput('date')
    infor_list = question.objects.all()
    return render_to_response('blog.html',{'date': date,'infor_list':infor_list})
    

def server(request):
     infor_list = Information.objects.all()
     return render_to_response('server.html',{'infor_list':infor_list})



def monitort(request):
     os.system('sh /home/zqxt_form2/monitor/image.sh')
     return render(request,'monitort.html')


def websshtest(request):
    if request.method == 'POST':
        form = websshform(request.POST)
        if form.is_valid():
            command = form.cleaned_data['command']
            if command.find('rm'):
                output = commands.getoutput(command)
                date=commands.getoutput('date') 
                return render(request, 'websshn.html', {'form': form,'output': output,'date':date})
            else:
                 rmdata="对不起，禁止删除！"
                 return render(request, 'websshn.html', {'rmdata':rmdata})
    else:
        form = websshform()
    return render(request, 'websshn.html', {'form': form})

    return render(request,'websshn.html')

def testRelease(request):
    return HttpResponse('测试环境发布成功')

def formalRelease(request):
    return HttpResponse('正式环境发布成功')


def servicemanage(request):
    return HttpResponse('程序启动成功')


def experience(request):
    date=commands.getoutput('date')
    infor_list = Experience.objects.all()
    return render_to_response('experience.html',{'date': date,'infor_list':infor_list})



def linuxlog(request):
    date=commands.getoutput('date')
    return render_to_response('linuxlog.html',{'date':date})

def servicelog(request):
    date=commands.getoutput('date')
    return render_to_response('servicelog.html',{'date':date})




def cpu(request):
    os.system('sh /home/zqxt_form2/monitor/image.sh')
    return render_to_response('cpu.html')

def memory(request):
    os.system('sh /home/zqxt_form2/monitor/image.sh')
    return render_to_response('memory.html')

def disk(request):
    os.system('sh /home/zqxt_form2/monitor/image.sh')
    return render_to_response('disk.html')



def show(request):
    infor_list = monitors.objects.all()
    return render_to_response('show.html',{'infor_list':infor_list})

def showcpu(request):
    infor_list = monitors.objects.all()
    for infor in infor_list:
        if infor.item =='cpu':
            cpuvalue=infor.value
            cpuip=infor.serverip
            os.environ['cpuip']=str(cpuip) 
            localcpu = commands.getoutput("sh /home/zqxt_form2/monitor/cpu2.sh  $cpuip")
            if int(cpuvalue) <  float(localcpu):
                return HttpResponse( str(cpuip)+'的cpu load 已经超过了阈值了,它的cpu  load值是：'+str(localcpu))
            else:
                return HttpResponse(str(cpuip)+'触发值还没达到报警值,它的cpu  load值是：'+str(localcpu))
        else:
            return HttpResponse('没有匹配到cpu监控项')
        

def showmemory(request):
    memory_list = monitors.objects.filter(item='memory')
    for mem in memory_list:
        if mem.item =='memory':
            memoryvalue=mem.value
            ip=mem.serverip
            os.environ['ip']=str(ip)
            localmemory = commands.getoutput("sh /home/zqxt_form2/monitor/memory3.sh  $ip")
            if int(memoryvalue) <  float(localmemory):
                return HttpResponse( str(ip)+'的memory已经超过了阈值了,它的memory值是：'+str(localmemory))
            else:
                return HttpResponse(str(ip)+'触发值还没达到报警值,它的memory值是：'+str(localmemory))
        else:
            return HttpResponse('没有匹配到memory监控项')



def showdisk(request):
    disk_list = monitors.objects.filter(item='disk')
    for disk in disk_list:
        if disk.item =='disk':
            diskvalue=disk.value
            ip=disk.serverip
            os.environ['ip']=str(ip)
            localdisk = commands.getoutput("sh /home/zqxt_form2/monitor/disk3.sh  $ip")
            if int(diskvalue) <  float(localdisk):
                return HttpResponse( str(ip)+'的磁盘已经超过了阈值:  '+str(diskvalue)+'它的disk值是：'+str(localdisk))
            else:
                return HttpResponse(str(ip)+'触发值还没达到报警值:'+str(diskvalue)+' ,它的disk值是：'+str(localdisk))
        else:
            return HttpResponse('没有匹配到disk监控项')


import json
def ajax_demo(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == '111' and pwd == '222':
            return HttpResponse(json.dumps())
        else:
            return HttpResponse(json.dumps(ret))
    return render(request,'ajax_demo.html')

def echart(request):
    if request.method == 'POST':
        data2 = {'month':'1yue','zf':'20'}
        return HttpResponse(json.dumps(data2))
    return render(request,'jqueryajax.html')

