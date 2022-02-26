from django.db import models
from user.models import User
from config.helpers import UploadTo


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='category')
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(default=0)
    count = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    size = models.CharField(max_length=100)
    description = models.TextField()
    total = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to=UploadTo('product'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total = self.price * self.count
        return super(Product, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'


class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='product')
    coupon = models.FloatField(default=0)
    shipping_fee = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total = ((self.product.price * self.coupon)/100) * self.product.price
        return super(Card, self).save(*args, **kwargs)

    