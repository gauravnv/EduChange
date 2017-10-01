from django.conf.urls import url

from . import views

app_name = 'vjk'
urlpatterns = [
    #/Hestia/
    url(r'^$', views.index, name='index'),

    # /Hestia/20/
    url(r'^(?P<Parent_id>[0-9]+$', views.detail, name='detail'),
]
