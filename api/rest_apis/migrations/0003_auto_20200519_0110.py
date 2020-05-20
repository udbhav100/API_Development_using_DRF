# Generated by Django 3.0.6 on 2020-05-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0002_auto_20200519_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='users',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
    ]
