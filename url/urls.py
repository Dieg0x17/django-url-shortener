from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.newuri, name='newuri'),
    url(r'^(?P<urlpk>\w{32})', views.geturi, name='geturi'), 


]
