# Generated by Django 3.2 on 2021-07-18 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20210718_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='account_created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]