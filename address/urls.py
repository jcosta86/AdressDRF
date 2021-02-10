from django.urls import include, path
from rest_framework import routers
from .views import CountryViewSet


router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]