from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'login$', views.login, name='login'),
    url(r'register/$', views.register, name='register'),

    # url(r'(?P<course_id>\d+)/delete/$', views.delete_course, name='delete')

]
