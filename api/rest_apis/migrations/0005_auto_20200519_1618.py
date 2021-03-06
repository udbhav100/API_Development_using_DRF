# Generated by Django 3.0.6 on 2020-05-19 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0004_auto_20200519_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(max_length=100)),
                ('medium_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('hobby_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='profileimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=32)),
                ('starts', models.DateField()),
                ('ends', models.DateField()),
                ('status', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('proficiency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=200)),
                ('aboutme', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
        migrations.DeleteModel(
            name='users_new',
        ),
        migrations.AddField(
            model_name='skills',
            name='users',
            field=models.ManyToManyField(to='rest_apis.userinfo'),
        ),
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_apis.userinfo'),
        ),
        migrations.AddField(
            model_name='profileimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_apis.userinfo'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='users',
            field=models.ManyToManyField(to='rest_apis.userinfo'),
        ),
        migrations.AddField(
            model_name='communication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_apis.userinfo'),
        ),
        migrations.AddField(
            model_name='achievements',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_apis.userinfo'),
        ),
    ]
