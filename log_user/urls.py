from django.conf.urls import url,include
from django.contrib import admin

from log_user import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', views.login1,name='login' ),
    url(r'^register/$', views.register1, name='register'),
    url(r'^regsuccess/$', views.register_sussess, name = 'success'),
    url(r'^logout/$', views.logout1, name='logout'),

    
    
    ]
