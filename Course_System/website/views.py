from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy

from datetime import datetime

from base_app.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', locals())
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if not User.exists(email):
            user = User(email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
        else:
            "User already exist"
            return render(request, 'login.html', locals())


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        u = User.login(email, password)

        if u is None:
            error = 'Wrong username/password'
        else:
            request.session['email'] = email
            response = redirect('website:profile')
            response.set_cookie('last_conection', datetime.now())
            response.set_cookie('username', email)

            return response
