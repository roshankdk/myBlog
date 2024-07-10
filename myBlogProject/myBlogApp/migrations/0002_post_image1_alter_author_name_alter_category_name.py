# Generated by Django 5.0.6 on 2024-07-09 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(default=datetime.datetime(2024, 7, 9, 7, 47, 46, 851023, tzinfo=datetime.timezone.utc), upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
