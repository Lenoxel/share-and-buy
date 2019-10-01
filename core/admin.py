from django.contrib import admin

from .models import Product, ProductAffiliated

admin.site.register(Product)
admin.site.register(ProductAffiliated)
