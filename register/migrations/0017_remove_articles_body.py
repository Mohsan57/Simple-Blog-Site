# Generated by Django 3.2 on 2021-07-31 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='body',
        ),
    ]
