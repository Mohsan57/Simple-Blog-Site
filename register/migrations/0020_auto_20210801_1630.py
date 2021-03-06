# Generated by Django 3.2 on 2021-08-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_articles_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='Hello World', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
