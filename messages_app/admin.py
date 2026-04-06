from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "sender", "receiver", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("subject", "body", "sender__username", "receiver__username")

# Register your models here.
