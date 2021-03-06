from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from . import models


class PlaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


admin.site.register(models.Place, PlaceAdmin)
admin.site.register(models.Service)
admin.site.register(models.PlaceService)
