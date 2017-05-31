from rest_framework import serializers
from pogon.models import Operater


class OperaterSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Operater
        fields = ("kreirao", "nalog", "sifra", "slika", "is_star")
