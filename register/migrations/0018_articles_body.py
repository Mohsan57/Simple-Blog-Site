# Generated by Django 3.2 on 2021-07-31 09:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_remove_articles_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='body',
            field=ckeditor.fields.RichTextField(default='asdas'),
            preserve_default=False,
        ),
    ]
