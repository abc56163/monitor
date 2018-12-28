from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MonitorInfo(models.Model):
    #crom = models.CharField(max_length=200,null=False, verbose_name='机房')
    user = models.CharField(max_length=10,null=False, verbose_name='用户')
    time = models.CharField(max_length=20, null=False, verbose_name='日期')
    router = models.CharField(max_length=10,null=False, verbose_name='路由器')
    switch = models.CharField(max_length=10,null=False, verbose_name='交换机')
    server = models.CharField(max_length=10,null=False, verbose_name='语音服务器')
    gateway = models.CharField(max_length=10,null=False, verbose_name='语言网关')
    ups = models.CharField(max_length=10,null=False, verbose_name='UPS')
    flow = models.CharField(max_length=10,null=False, verbose_name='流控')
    air = models.CharField(max_length=10,null=False, verbose_name='空调')
    temperature = models.CharField(max_length=10,null=False, verbose_name='温度')
    humidity = models.CharField(max_length=10,null=False, verbose_name='湿度')
    remark = models.TextField(null=True, verbose_name='备注')

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s' %(self.time,self.router,self.switch,
        self.server, self.gateway, self.ups, self.flow, self.air, self.temperature, self.humidity,
        self.remark)



# class Device(models.Model):
#     user = models.OneToOneField(User,unique=True)
#     deviceadd = models.CharField(max_length=20,null=False, verbose_name='设备地址')


