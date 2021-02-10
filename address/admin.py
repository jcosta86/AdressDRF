from django.contrib import admin
from address.models import Country, State, City, District, Address


class CountryAdmin(admin.ModelAdmin):
    list_display = ('description',)


class StateAdmin(admin.ModelAdmin):
    list_display = ('description',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('description',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('description',)


class AddresstAdmin(admin.ModelAdmin):
    list_display = ('description', 'number', 'cep')


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Address, AddresstAdmin)
