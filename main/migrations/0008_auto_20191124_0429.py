# Generated by Django 2.2 on 2019-11-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
