# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#
# ]

from django.urls import path
from django.conf.urls import url
from .views import current_user, UserList, RegisterView
from . import views

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),


]