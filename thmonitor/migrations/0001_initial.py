# Generated by Django 2.1.3 on 2018-12-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10, verbose_name='用户')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
                ('router', models.CharField(max_length=10, verbose_name='路由器')),
                ('switch', models.CharField(max_length=10, verbose_name='交换机')),
                ('server', models.CharField(max_length=10, verbose_name='语音服务器')),
                ('gateway', models.CharField(max_length=10, verbose_name='语言网关')),
                ('ups', models.CharField(max_length=10, verbose_name='UPS')),
                ('flow', models.CharField(max_length=10, verbose_name='流控')),
                ('air', models.CharField(max_length=10, verbose_name='空调')),
                ('temperature', models.CharField(max_length=10, verbose_name='温度')),
                ('humidity', models.CharField(max_length=10, verbose_name='湿度')),
                ('remark', models.TextField(null=True, verbose_name='备注')),
            ],
        ),
    ]
