from django.contrib import admin
from store.models import Product, Order, Cart, Category, ShippingAddress

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'categorie', 'date_added')

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'user', 'address', 'email', 'city', 'state')
# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(ShippingAddress, AdminCommande)