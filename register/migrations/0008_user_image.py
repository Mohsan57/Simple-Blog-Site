# Generated by Django 3.2 on 2021-07-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_alter_register_account_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
