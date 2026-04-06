from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade


@login_required
def grades_list(request):
    items = Grade.objects.filter(student=request.user).select_related('course')
    return render(request, 'grades/list.html', {"items": items})

# Create your views here.
