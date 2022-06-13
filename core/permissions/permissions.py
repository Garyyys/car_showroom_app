from rest_framework import permissions


class IsCustomerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_customer


class IsShowroomUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_showroom


class IsDealerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_supplier
