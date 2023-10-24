# Generated by Django 4.2.6 on 2023-10-24 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_article_blog_picture_alter_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_picture',
            field=models.ImageField(blank=True, default='images/none_picture', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 24, 9, 59, 9, 865024, tzinfo=datetime.timezone.utc)),
        ),
    ]
