# Generated by Django 4.1.1 on 2022-10-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_event_remove_post_author_remove_post_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10, null=True),
        ),
    ]
