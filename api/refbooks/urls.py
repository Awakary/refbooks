from django.urls import include, path, re_path
from rest_framework import routers

from refbooks.views import ElementRefBookViewSet, RefBookViewSet

#
# router = routers.DefaultRouter()
# router.register(r'', RefBookViewSet, basename='refbolll')
# router.register(/'elements', ElementRefBookViewSet, basename='elements')


urlpatterns = [
    path(r'', RefBookViewSet.as_view({'get': 'list'})),
    path(r'<int:id>/elements/', ElementRefBookViewSet.as_view({'get': 'list'})),
    path(r'<int:id>/check_element/', ElementRefBookViewSet.as_view({'get': 'check_element'}))
]
