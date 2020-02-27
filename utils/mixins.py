from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class DefaultMixin:
    authentication_classes =  (SessionAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class StandartResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000