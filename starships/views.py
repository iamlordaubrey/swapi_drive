from rest_framework import generics

from starships.models import Starship
from starships.serializers import StarshipSerializer


class StarshipList(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
