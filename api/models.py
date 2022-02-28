from django.db import models
from user.models import User
from config.helpers import UploadTo
from user.validators import PhoneValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='category')
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(default=0)
    count = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    size = models.CharField(max_length=100)
    description = models.TextField()
    total = models.PositiveBigIntegerField(default=0)
    picture = models.ImageField(upload_to=UploadTo('product'))
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.product.price-((self.product.price * self.coupon)/100)
        return super(Card, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    address = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=13, unique=True, validators=[PhoneValidator()])
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    products = models.ManyToManyField(Product, related_name='products')
    price = models.PositiveBigIntegerField(default=0)
    count = models.IntegerField(default=0)
    total = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.price * self.count
        return super(OrderProduct, self).save(*args, **kwargs)
    
