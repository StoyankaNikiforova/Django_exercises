from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'new$', views.add_course, name='new'),
    url(r'(?P<course_id>\d+)/delete/$', views.delete_course, name='delete'),
    url(r'edit_course/(?P<course_id>\d+)/$', views.edit_course, name='edit')


]
