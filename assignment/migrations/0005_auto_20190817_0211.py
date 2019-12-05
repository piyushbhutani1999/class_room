# Generated by Django 2.2.4 on 2019-08-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_auto_20190817_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='instructions',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]