# Generated by Django 3.2 on 2021-08-03 07:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_rename_body_articles_contant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='contant',
            field=ckeditor.fields.RichTextField(verbose_name='body'),
        ),
    ]
