from django.contrib import admin

from .models import Product, Manufacturer, Affiliated

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Affiliated)
