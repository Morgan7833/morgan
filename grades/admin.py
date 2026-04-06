from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "grade")
    list_filter = ("course",)
    search_fields = ("student__username", "course__code")

# Register your models here.
