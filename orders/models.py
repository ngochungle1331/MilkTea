from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
STATUS = (
    ('Pending', 'Pending'),
    ('Prepared', 'Prepared'),
    ('Shipping', 'Shipping'),
    ('Delivered', 'Delivered')
)

CATEGORIES = (
    ('TRÀ SỮA', 'TRÀ SỮA'),
    ('SODA', 'SODA'),
    ('SỮA TƯƠI', 'SỮA TƯƠI'),
    ('TRÀ TRÁI CÂY', 'TRÀ TRÁI CÂY'),
    ('ĐỒ ĂN VẶT', 'ĐỒ ĂN VẶT'),
    ('THỨC UỐNG KHÁC', 'THỨC UỐNG KHÁC')
)

AVAILABILITIES = (
    ('có sẵn', 'có sẵn'),
    ('không có sẵn', 'không có sẵn'),
    ('sắp ra mắt', 'sắp ra mắt')
)

class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=32, choices=CATEGORIES, default='TRÀ SỮA')
    price = models.IntegerField(default=50000) 
    unit = models.CharField(max_length=10, default='1 ly')
    availability = models.CharField(max_length=32, choices=AVAILABILITIES, default='có sẵn')
    quantity = models.IntegerField()
    description_short = models.CharField(max_length=64, default='có sẵn')
    description_long = models.TextField(default='có sẵn')
    # if not image then use a default image, consider to have a site to let administrators change image and content/description
    image = models.ImageField(verbose_name="Product Image", upload_to="orders/static/orders/images/", default=None, blank=True)
    image_filename = models.CharField(max_length=256, default="image.jpg")

    def __str__(self):
        return f"{self.name} - {self.price}"

class Ordered_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField()
    price_quantity = models.IntegerField()
    # customer needs: less ice, more ice. Together with ice or not. Extra comment
    # create a JSON format here
    notice = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernames")
    ordered_items = models.ManyToManyField(Ordered_item, blank=True, related_name="items")
    name = models.CharField(max_length=32, blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    shipping_address = models.TextField(blank=True)
    email = models.CharField(max_length=64, blank=True)
    total_price = models.IntegerField()
    ordered_time = models.DateTimeField(auto_now_add=True)
    expected_time_request = models.TextField(blank=True)
    # decide by administrators
    delivery_time = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, choices=STATUS, default='Pending')

