from django.contrib import admin
from .models import MysqlAppModel
# Register your models here.

@admin.register(MysqlAppModel)
class MysqlAppModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']