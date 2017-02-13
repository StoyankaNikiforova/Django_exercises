from django.shortcuts import render
from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', locals())


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


# def update_course(request, id):
#    emp = Employee.objects.get(pk = id)
#    #you can do this for as many fields as you like
#    #here I asume you had a form with input like <input type="text" name="name"/>
#    #so it's basically like that for all form fields
#    emp.name = request.POST.get('name')
#    emp.save()
#    return HttpResponse('updated')

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    return render(request, 'index.html', locals())
