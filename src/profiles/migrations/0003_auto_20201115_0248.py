# Generated by Django 3.1.3 on 2020-11-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201115_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='blogify.jpeg', upload_to='profile_photos/'),
        ),
    ]
