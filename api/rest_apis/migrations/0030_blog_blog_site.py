# Generated by Django 3.0.6 on 2020-06-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_apis', '0029_education_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_site',
            field=models.TextField(default='medium'),
            preserve_default=False,
        ),
    ]