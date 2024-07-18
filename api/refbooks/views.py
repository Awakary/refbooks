from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from refbooks.models import ElementRefBook, RefBook
from refbooks.serializers import ElementRefBookSerializer, RefBookSerializer


class RefBookViewSet(ListModelMixin, GenericViewSet):

    def get_queryset(self):
        date_check = self.request.query_params.get('date', None)

        if date_check:
            return RefBook.objects.filter(versions__start_date__lte=date_check).distinct()
        return RefBook.objects.all()
    serializer_class = RefBookSerializer

    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('date',
                                             type=openapi.TYPE_STRING,
                                             in_=openapi.IN_QUERY,
                                             description='Дата в формате ГГГГ-ММ-ДД')
                           ])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'refbooks': serializer.data})


class ElementRefBookViewSet(ListModelMixin, RetrieveModelMixin,
                            GenericViewSet):

    queryset = ElementRefBook.objects.all()
    serializer_class = ElementRefBookSerializer

    def filter_queryset(self, queryset):
        refbook_id = self.kwargs.get('id', None)
        version = self.request.query_params.get('version', None)
        queryset = ElementRefBook.objects.filter(version__refbook=refbook_id)
        if version:
            return queryset.filter(version__number=version)
        refbook = RefBook.objects.get(pk=refbook_id)
        if not refbook.current_version:
            raise ValueError('Нет текущей версии справочника')
        return queryset.filter(version__number=refbook.current_version.number)

    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('id',
                                             type=openapi.TYPE_INTEGER,
                                             in_=openapi.IN_PATH,
                                             required=True,
                                             description='Идентификатор справочника'),
                           openapi.Parameter('version',
                                             type=openapi.TYPE_STRING,
                                             required=False,
                                             in_=openapi.IN_QUERY,
                                             description='Версия справочника')
                           ])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'elements': serializer.data})

    @method_decorator(name='retrieve', decorator=swagger_auto_schema(
        operation_description='Валидация элемента справочника',
        manual_parameters=[openapi.Parameter('id',
                                             type=openapi.TYPE_INTEGER,
                                             in_=openapi.IN_PATH,
                                             required=True,
                                             description='Идентификатор справочника'),
                           openapi.Parameter('code',
                                             type=openapi.TYPE_STRING,
                                             in_=openapi.IN_QUERY,
                                             required=True,
                                             description='Код элемента справочника'),
                           openapi.Parameter('value',
                                             type=openapi.TYPE_STRING,
                                             in_=openapi.IN_QUERY,
                                             required=True,
                                             description='Значение элемента справочника'),
                           openapi.Parameter('version',
                                             type=openapi.TYPE_STRING,
                                             in_=openapi.IN_QUERY,
                                             description='Версия справочника')
                           ]
    ))
    def check_element(self, request, *args, **kwargs):
        code = self.request.query_params.get('code', None)
        value = self.request.query_params.get('value', None)
        search_queryset = self.filter_queryset(self.queryset)
        element = search_queryset.filter(code=code, value=value)
        if not element.exists():
            raise ValueError('Нет элемента с данным кодом и значением')
        serializer = self.get_serializer(element[0])
        return Response(serializer.data)
