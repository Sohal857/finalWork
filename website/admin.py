from django.contrib import admin

from .models import Content
from .models import Product
from .models import Category
from django_summernote.admin import SummernoteModelAdmin

class ContentAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'mod_date')
    summernote_fields = ('body')

admin.site.register(Content, ContentAdmin)

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'mod_date')
    summernote_fields = ('description', 'features')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)
