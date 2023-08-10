from django.contrib import admin
from ecommerce.models import Category, Products
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'active')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'price', 'prod_category')
    search_fields = ('name',)
    
admin.site.register(Category)
admin.site.register(Products)