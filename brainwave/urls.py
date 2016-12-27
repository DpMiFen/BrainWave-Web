from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
    url(r'^choice$', views.choice, name='choice'),
    url(r'^create_qrcode$', views.create_qrcode, name='create'),
]