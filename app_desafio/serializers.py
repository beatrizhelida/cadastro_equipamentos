from rest_framework import serializers
from .models import Equipamento

class DesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'
class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'
    def validate(self, data):
        required_fields = ['tipo', 'fabricante', 'modelo', 'numero_serie']
        errors = {}
        for field in required_fields:
            if not data.get(field):
                errors[field] = 'Campo obrigatório.'
        if errors:
            raise serializers.ValidationError(errors)
        return data