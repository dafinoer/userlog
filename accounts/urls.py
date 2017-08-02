from django.conf.urls import url
from .views import regist_user,login_user

urlpatterns = [
    url(r'^register$', regist_user, name='register'),
    url(r'^login$', login_user, name='login'),

]
