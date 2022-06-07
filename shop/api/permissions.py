from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAdminUser

#
# class IsSeller(BasePermission):
#     """
#         Access only to seller or admin
#     """
#     def has_permission(self, request, view):
#         return bool(
#             IsAdminUser or
#         )
