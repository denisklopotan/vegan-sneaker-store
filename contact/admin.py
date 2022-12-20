from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email', 'subject', 'body')
    list_filter = ('name', 'email')
