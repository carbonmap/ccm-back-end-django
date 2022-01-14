from rest_framework import permissions
from .models import UserToEntity

class UserEntityPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        matches = UserToEntity(entity_id=obj.id, user_id=request.user.id)
        if matches.objects.length > 0:
            return True 

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        return False
