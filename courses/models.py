from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='enrolled_courses', blank=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.code} - {self.name}"

# Create your models here.
