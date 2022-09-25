from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon (models.Model):
    '''coupon to add to purchase'''
    code = models.CharField(max_length=50, unique=True, null=True)
    valid_from = models.DateTimeField(null=True)
    valid_to = models.DateTimeField(null=True)
    discount = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    
    active = models.BooleanField(null=True)

    def __str__(self):
        return self.code

# class Coupon (models.Model):
#     '''coupon to add to purchase'''
#     coupon_code = models.CharField(max_length= 10)
#     is_expired = models.BooleanField(default=False)
#     discount_price = models.IntegerField(default=100)
#     minimum_amount = models.IntegerField(default=500)

