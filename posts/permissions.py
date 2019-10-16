from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object-permission(self, request, view, obj):
        # read only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissiona are only allowed for author

        return obj.author == request.user
