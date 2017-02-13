from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'new$', views.add_course, name='new'),
    url(r'(?P<course_id>\d+)/delete/$', views.delete_course, name='delete')

]
