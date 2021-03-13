from django.contrib import admin
from .models import *



class ImageInline(admin.TabularInline):
    model = AddressImage
    fields = ('address_image',)


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]