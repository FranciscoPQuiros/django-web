from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^<username>$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^registro/$', views.registro, name='registro')
]
