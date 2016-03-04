from django.conf.urls import url

from . import views
app_name = 'student'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^1/$', views.read, name='read'),
    url(r'^2/$', views.search, name='search'),
]
