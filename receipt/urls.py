from django.conf.urls import url,include
from django.contrib import admin
from receipt import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^receipt-list/$', views.lista_paragonow, name='lista_paragonow'),
    url(r'^receipt-form/$', views.add_receipt, name='add_receipt'),
    ]
