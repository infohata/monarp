from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_google_maps import fields as map_fields
from tinymce.models import HTMLField


class Place(models.Model):
    owner = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("owner"), 
        on_delete=models.CASCADE,
        related_name='places',
    )

    name = models.CharField(_("name"), max_length=200)
    address = map_fields.AddressField(_("address"), max_length=200, null=True, blank=True)
    geolocation = map_fields.GeoLocationField(
        _("location coordinates"), 
        max_length=100,
        blank=True,
        null=True,
    )
    notes = HTMLField(_("notes"), blank=True, )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.name
