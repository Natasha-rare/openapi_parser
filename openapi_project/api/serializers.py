# serializers.py
from collections import OrderedDict

from rest_framework import serializers
from .models import Cinemas

class CinemasSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cinemas
        fields = '__all__'

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields
        dict_translate = {'cinema_name': 'Название', 'address': 'Адрес',
                          'description': 'Примечания', 'legal_entity': 'Юридическое лицо', 'website': 'Сайт',
                          'category': 'Категория', 'inn': 'ИНН'}
        for field in fields:
            if field.field_name == 'id':
                continue
            attribute = field.get_attribute(instance)
            ret[dict_translate[field.field_name]] = attribute
        return ret