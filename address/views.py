from rest_framework import viewsets
from address.models import Country, State, City, Address
from address.serializers import CountrySerializer, StateSerializer, CitySerializer \
    , DistrictSerializer, AddressSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Show all countries."""
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ModelViewSet):
    """Show all states."""
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    """Show all cities."""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    """Show all districts."""
    queryset = State.objects.all()
    serializer_class = DistrictSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """Show all address."""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
