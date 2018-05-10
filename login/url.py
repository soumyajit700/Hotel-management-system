
from . import views
from django.conf.urls import url
app_name = 'login'
urlpatterns = [
     url(r'^$', views.start, name='Start'),
     url(r'^login/$', views.login_user, name='login'),
     url(r'^register/$', views.register, name='register'),
     url(r'^book/$', views.hotel, name='hotel')

]