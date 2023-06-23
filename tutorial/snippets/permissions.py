from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        """
        Read persmissions are allowed to any request,
        so we will always allow GET, HEAD or OPTIONS requests.
        Write permissions are only allowed to the owner of the snippet
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user