# Generated by Django 4.1.1 on 2022-09-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='active',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='code',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='valid_from',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='valid_to',
        ),
        migrations.AddField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount_price',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='coupon',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupon',
            name='minimum_amount',
            field=models.IntegerField(default=500),
        ),
    ]
