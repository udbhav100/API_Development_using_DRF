# Generated by Django 3.0.6 on 2020-06-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0024_auto_20200616_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='ContactNo',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Total_Experience',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='employeeid',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='industries',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='joiningdate',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='summary',
        ),
    ]
