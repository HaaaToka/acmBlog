from django.conf.urls import url
from .views import *

app_name='accounts'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', logout_view, name='logout'),

]
