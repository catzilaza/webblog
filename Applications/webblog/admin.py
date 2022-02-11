from django.contrib import admin
from Applications.webblog.models import WebblogFormModel


# Register your models here.

@admin.register(WebblogFormModel)
class WebblogFormModel(admin.ModelAdmin):
    list_display = ['topic', 'content', 'name', 'email', 'post_date']