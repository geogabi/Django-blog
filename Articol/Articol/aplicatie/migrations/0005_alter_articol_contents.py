# Generated by Django 4.2.5 on 2023-09-15 14:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie', '0004_articol_contents_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articol',
            name='contents',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]