# Generated by Django 4.1.1 on 2022-09-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_remove_post_title_post_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sku',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
