from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from ecommerce.settings import AUTH_USER_MODEL

class Category(models.Model):
    title = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']



class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})



class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
       return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def get_cart_total(self):
        return sum([order.product.price * order.quantity for order in self.orders.all()])


    def get_ordertotal(self):
        return sum([order.quantity for order in self.orders.all()])

    def __str__(self):
       return self.user.username

    def delete(self, *args, **kwargs):

        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()
        #super().clear(*args, **kwargs)


class ShippingAddress(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.CharField(max_length=300)
    address = models.CharField(max_length=120)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address




