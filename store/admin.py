from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_at', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Products, ProductsAdmin)