# Generated by Django 4.1.1 on 2022-11-28 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0013_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='event',
            name='topped',
        ),
    ]
