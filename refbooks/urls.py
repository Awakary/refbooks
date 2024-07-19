from django.urls import include, path, re_path
from rest_framework import routers

from refbooks.views import ElementRefbookViewSet, RefbookViewSet


urlpatterns = [
    path(r'', RefbookViewSet.as_view({'get': 'list'})),
    path(r'<int:id>/elements/', ElementRefbookViewSet.as_view({'get': 'list'})),
    path(r'<int:id>/check_element/', ElementRefbookViewSet.as_view({'get': 'check_element'}))
]
