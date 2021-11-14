# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#
# ]

from django.urls import include, path
from rest_framework import routers
from . import views
from .views import current_user, UserList

router = routers.DefaultRouter()
router.register(r'reporting_entity', views.ReportingEntityViewSet)

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


