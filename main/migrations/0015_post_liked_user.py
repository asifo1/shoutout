# Generated by Django 2.2 on 2019-12-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20191205_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(blank=True, to='main.Profile'),
        ),
    ]
