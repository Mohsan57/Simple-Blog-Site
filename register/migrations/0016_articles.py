# Generated by Django 3.2 on 2021-07-31 07:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_alter_register_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='articles')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
