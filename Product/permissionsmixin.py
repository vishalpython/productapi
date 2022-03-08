from rest_framework import permissions
from django.contrib.auth import get_user_model
from User.models import User


class PermissionView(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(id=request.user.id)
        if user.is_active and user.is_staff:
            return True
        elif user.is_active and request.method in ['POST', 'GET', 'PUT']:
            return True
        elif request.method in ['POST', 'GET']:
            return True
        return False
