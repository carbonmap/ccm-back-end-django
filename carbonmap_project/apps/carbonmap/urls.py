# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#
# ]

from django.urls import include, path
from . import views
from .views import current_user, UserList, ReportingEntityViewSet, ReportingEntityAddressViewSet

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reporting_entity/', ReportingEntityViewSet.as_view({'get':'list', 'post':'create'})),
    path('reporting_entity/<str:pk>/', ReportingEntityViewSet.as_view(
        {'get':'retrieve', 'put':'update'})),
    path('reporting_entity/<str:pk>/address/', ReportingEntityAddressViewSet.as_view(
        {'get':'retrieve', 'put':'update'})),
]


