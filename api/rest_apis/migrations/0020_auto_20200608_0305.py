# Generated by Django 3.0.3 on 2020-06-07 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0019_auto_20200605_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='Imageupload',
        ),
        migrations.DeleteModel(
            name='profileimage',
        ),
    ]
