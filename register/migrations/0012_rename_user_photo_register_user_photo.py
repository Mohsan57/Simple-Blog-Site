# Generated by Django 3.2 on 2021-07-19 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20210719_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='User_Photo',
            new_name='user_photo',
        ),
    ]