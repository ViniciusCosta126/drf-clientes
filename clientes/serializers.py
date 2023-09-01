from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "Numero de cpf invalido"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {"nome": "O campo nome não deve ter numeros"})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': 'O rg deve ter 9 digitos'})

        if not numero_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': 'O numero de celular deve seguir esse modelo: 11 91234-1234'})
        return data
