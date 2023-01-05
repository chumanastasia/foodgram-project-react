from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    """ Allow admin to edit, but not other users """
    @staticmethod
    def has_permission(request, view):
        """Check if user is admin"""
        return request.method in SAFE_METHODS or request.user.is_staff


class IsAuthorOrReadOnly(BasePermission):
    """ Allow author to edit, but not other users """

    @staticmethod
    def has_permission(request, view):
        """Check if user authenticated and has permission."""
        return request.method in SAFE_METHODS or request.user.is_authenticated

    @staticmethod
    def has_object_permission(request, view, obj):
        """Check if user is author of the object"""
        return obj.author == request.user
