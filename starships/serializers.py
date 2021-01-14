from rest_framework import serializers

from starships.models import Starship


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = ('name', 'model', 'manufacturer', 'hyperdrive_rating')
