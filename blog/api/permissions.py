from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            IsAdminUser and IsAuthenticated and obj.owner == request.user
            or IsSuperUser
        )


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            IsAuthenticated and request.user.is_superuser
        )

