from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    """
    Custom permission to only allow admins to edit objects.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class ReviewUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the review owner to edit it.
    Assumes the model instance has an `review_user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the review owner
        else:
            return obj.review_user == request.user