# Generated by Django 3.2 on 2021-08-03 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_alter_articles_contant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='contant',
            new_name='content',
        ),
    ]
