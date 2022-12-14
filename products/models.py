"""
This model for products app
"""
from django.db import models


class Category(models.Model):
    """
    name for programming
    """

    class Meta:
        """modify Django model spelling issue"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """friendly name for easy to read"""
        return self.friendly_name


class Product(models.Model):
    """product display details"""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
