from rest_framework import viewsets
from address.models import Country
from address.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Show all countries."""
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer

