from rest_framework.serializers import ModelSerializer

from refbooks.models import ElementRefbook, Refbook


class RefbookSerializer(ModelSerializer):

    class Meta:
        model = Refbook
        fields = ['id', 'code', 'name']


class ElementRefbookSerializer(ModelSerializer):

    class Meta:
        model = ElementRefbook
        fields = ['code', 'value']