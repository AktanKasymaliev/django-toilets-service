from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, obj, view):
        return request.user.is_authenticated and request.user == view.username

class IsCommentOwnerOrPostAdmin(BasePermission):
    def has_object_permission(self, request, obj, view):
        return request.user.is_authenticated and request.user == view.owner