# Generated by Django 3.1.6 on 2021-04-18 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmanager', '0008_menu_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='picture',
        ),
    ]
