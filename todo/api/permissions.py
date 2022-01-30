from rest_framework import permissions


# 
class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        print("request: ", request.user.is_authenticated)
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

class IsMyselfToRetrieveUpdateDestroy(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        """自身のみがGET（詳細）・PUT・PATCH・DELETE許可"""
        return obj == request.user