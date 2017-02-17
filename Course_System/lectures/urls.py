from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lectures, name='lectures'),
    url(r'^new_lecture$', views.add_lecture, name='new_lecture'),
    url(r'(?P<lecture_id>\d+)/delete/$', views.delete_lecture, name='delete_lecture'),
    url(r'(?P<lecture_id>\d+)$', views.edit_lecture, name='edit_lecture'),
    url(r'update_lecture/(?P<lecture_id>\d+)$', views.update_lecture, name='update_lecture'),
]
