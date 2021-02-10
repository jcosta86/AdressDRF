from django.urls import include, path
from rest_framework import routers
from .views import CountryViewSet, StateViewSet, CityViewSet, DistrictViewSet, AddressViewSet

router = routers.DefaultRouter()

router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'states', StateViewSet, basename='states')
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'districts', DistrictViewSet, basename='districts')
router.register(r'address', AddressViewSet, basename='address')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
