from django.conf.urls import url

from . import views

app_name = 'find_cat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pet_id>[0-9]+)/$', views.detail, name='detail'),
    ]