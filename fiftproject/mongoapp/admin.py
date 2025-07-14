from django.contrib import admin
from .models import MongoAppModel
# Register your models here.

@admin.register(MongoAppModel)
class MongoAppModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']