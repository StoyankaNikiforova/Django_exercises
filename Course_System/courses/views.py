from django.shortcuts import render
from courses.models import Course


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', locals())


def add_course(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        course = Course(name=name, discription=description, start_date=start_date, end_date=end_date)
        course.save()
    return render(request, 'new.html', locals())


def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('course_name')
        course.description = request.POST.get('course_description')
        course.start_date = request.POST.get('start_date')
        course.end_date = request.POST.get('end_date')

        course.save()

    return render(request, 'edit_course.html', locals())


def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    return render(request, 'index.html', locals())
