from rest_framework import permissions


class IsSeller(permissions.BasePermission):
    """
    Object-level permission to only allow publishers of a book data to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user
