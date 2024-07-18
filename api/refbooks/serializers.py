from rest_framework.serializers import ModelSerializer

from refbooks.models import ElementRefBook, RefBook


class RefBookSerializer(ModelSerializer):

    class Meta:
        model = RefBook
        fields = ['id', 'code', 'name']

    # def to_representation(self, instance):
    #     result = super(RefBookSerializer, self).to_representation(instance)
    #     return {'refbooks': [result]}

class ElementRefBookSerializer(ModelSerializer):

    class Meta:
        model = ElementRefBook
        fields = ['code', 'value']