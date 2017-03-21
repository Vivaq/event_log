from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_db, name='show_db'),
    url(r'^add_log/$', views.add_log, name='add_log')
]
