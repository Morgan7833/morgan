from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course


@login_required
def course_list(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            try:
                course = Course.objects.get(pk=course_id)
                course.students.add(request.user)
            except Course.DoesNotExist:
                pass
        return redirect('courses:list')
    courses = Course.objects.all()
    my_ids = set(request.user.enrolled_courses.values_list('id', flat=True))
    return render(request, 'courses/list.html', {"courses": courses, "my_ids": my_ids})

# Create your views here.
