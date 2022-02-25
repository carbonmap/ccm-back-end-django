from rest_framework import permissions
from .models import UserToEntity
#Uncomment to print passed object and lookup results
#from .serializers import ReportingEntitySerializer, UserToEntitySerializer
#from rest_framework.renderers import JSONRenderer

class UserEntityPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        #See https://docs.djangoproject.com/en/4.0/topics/db/queries/
        matches = UserToEntity.objects.filter(entity_id=obj.id, user_id=request.user.id)
        #Uncomment to print passed object and the results of the lookup
        #Note that in the API Browser, this method is called four times on each view to check the user
        #permissions
        #print(JSONRenderer().render(ReportingEntitySerializer(obj).data))
        #print(JSONRenderer().render(UserToEntitySerializer(matches,many=True).data))

        if len(matches) > 0:
            return True 

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False
