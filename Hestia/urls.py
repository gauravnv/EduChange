from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings

#app_name = 'Hestia'
urlpatterns = [
    #/Hestia/
    url(r'^$', views.index, name='index'),

    # /Hestia/2
    url(r'^(?P<User_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^condition/$', views.condition, name='condition'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
