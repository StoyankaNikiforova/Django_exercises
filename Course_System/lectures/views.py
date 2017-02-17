from django.shortcuts import render
from lectures.models import Lecture
from courses.models import Course
from django.http import HttpResponse
from .forms import NewLectureForm


def lectures(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures.html', locals())


def add_lecture(request):
    form = NewLectureForm()
    if request.method == 'POST':
        name = request.POST.get('lecture_name')
        week_number = request.POST.get('week')
        course_name = request.POST.get('course_name')
        url = request.POST.get('lecture_url')

        course = Course.objects.get(name=course_name)
        lecture = Lecture(name=name, week=week_number, course=course, url=url)
        lecture.save()
    return render(request, 'new_lecture.html', locals())


def edit_lecture(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    if request.method == 'POST':
        lecture.name = request.POST.get('lecture_name')
        lecture.week = request.POST.get('week')
        course_name = request.POST.get('course_name')
        lecture.url = request.POST.get('lecture_url')

        course = Course.objects.get(name=course_name)
        lecture.course = course
        lecture.save()

    return render(request, 'edit_lecture.html', locals())


def update_lecture(request, lecture_id):

    lecture = Lecture.objects.get(pk=lecture_id)
    import ipdb; ipdb.set_trace()
    lecture.name = request.POST.get('lecture_name')
    lecture.week = request.POST.get('week')
    course_name = request.POST.get('course_name')
    lecture.url = request.POST.get('lecture_url')

    course = Course.objects.get(name=course_name)
    lecture.course = course
    import ipdb; ipdb.set_trace()
    lecture.save()
    return HttpResponse('updated')


def delete_lecture(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    lecture.delete()
    return render(request, 'lectures.html', locals())
