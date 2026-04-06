from django.db import models
from django.conf import settings
from courses.models import Course


class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=10)
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.student} - {self.course}: {self.grade}"

# Create your models here.
