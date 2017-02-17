from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^lectures/', include('lectures.urls')),
    url(r'^website/', include('website.urls'))
]
