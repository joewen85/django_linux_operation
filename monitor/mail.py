# coding:utf-8
import os
import commands
from models import monitors

def cpumail():
    infor_list = monitors.objects.all()
    for infor in infor_list:
        if infor.item =='cpu':
            cpuvalue=infor.value
            cpuip=infor.serverip
            os.environ['cpuip']=str(cpuip) 
            localcpu = commands.getoutput("sh /home/zqxt_form2/monitor/cpu2.sh  $cpuip")
            if int(cpuvalue) <  float(localcpu):
                os.system('cat /home/zqxt_form2/monitor/mail.txt|mail -s "触发报警阀值"  961769710@qq.com')
            else:
                os.system('cat /home/zqxt_form2/monitor/mail.txt|mail -s "cpu的使用率还很ok"  961769710@qq.com')

