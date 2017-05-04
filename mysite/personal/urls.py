from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^CV/$', views.CV, name='CV'),
    url(r'^VBA/$', views.VBA, name='VBA'),
    url(r'^LaTeX/$', views.LaTeX, name='LaTeX'),
    url(r'^Pytuts/$', views.Pytuts, name='Pytuts'),
    url(r'^django/$', views.django, name='django'),
    url(r'^extra/$', views.extra, name='extra'),
    url(r'^safety/$', views.safety, name='safety'),
    url(r'^forecast/$', views.forecasttable, name='forecast'),
]
