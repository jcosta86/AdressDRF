from django.contrib import admin
from address.models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('description', )


admin.site.register(Country, CountryAdmin)
