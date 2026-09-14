from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ConatactAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
    list_filter = ['last_name']
    list_display_links = ['last_name', 'first_name']
