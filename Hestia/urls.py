from django.conf.urls import url

from . import views

app_name = 'vjk'
urlpatterns = [
    #/Hestia/
    url(r'^$', views.index, name='index'),


]
