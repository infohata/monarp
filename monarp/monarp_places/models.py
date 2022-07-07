from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_google_maps import fields as map_fields
from tinymce.models import HTMLField
from model_utils import Choices


PRICE_RANGE_CHOICES = Choices(
    (0, 'free', _("free")),
    (1, 'dirty_cheap', _("dirty cheap")),
    (2, 'cheap', _("cheap")),
    (3, 'affordable', _("affordable")),
    (4, 'expensive', _("expensive")),
    (5, 'sky_high', _("sky high")),
)


class Place(models.Model):
    owner = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("owner"), 
        on_delete=models.SET_NULL,
        related_name='owned_places',
        null=True, blank=True,
    )
    reported_by = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("reported by"), 
        on_delete=models.SET_NULL,
        related_name='reported_places',
        null=True, blank=True,
    )
    name = models.CharField(_("name"), max_length=200)
    address = map_fields.AddressField(_("address"), max_length=200, null=True, blank=True)
    geolocation = map_fields.GeoLocationField(
        _("location coordinates"), 
        max_length=100,
        blank=True,
        null=True,
    )
    description = HTMLField(_("notes"), blank=True, )
    website = models.URLField(_("website"), blank=True, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    is_active = models.BooleanField(_("is active"), default=True)
    is_private = models.BooleanField(_("is private"), default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(_("name"), max_length=63)
    icon = models.ImageField(_("icon"), upload_to='places/services/img')

    def __str__(self):
        return self.name


class PlaceService(models.Model):
    place = models.ForeignKey(
        Place, 
        verbose_name=_("place"), 
        on_delete=models.CASCADE,
        related_name='services',
    )
    service = models.ForeignKey(
        Service, 
        verbose_name=_("service"), 
        on_delete=models.CASCADE,
        related_name='places',
    )
    description = HTMLField(_("description"), blank=True)
    open_from = models.TimeField(_("open from"), default="0:00")
    open_until = models.TimeField(_("open until"), default="0:00")
    price = models.DecimalField(
        _("price"), 
        max_digits=12, 
        decimal_places=2, 
        null=True, blank=True,
        help_text=_("in local currency only, set zero for free, don't enter if unknown"),
    )
    price_range = models.PositiveSmallIntegerField(
        _("price range"), 
        choices=PRICE_RANGE_CHOICES, 
        default=PRICE_RANGE_CHOICES.free,
    )
    reported_by = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("reported by"), 
        on_delete=models.SET_NULL,
        related_name='reported_services',
        null=True, blank=True,
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    is_active = models.BooleanField(_("is active"), default=True)

    def __str__(self):
        return '{}: {}'.format(str(self.place), str(self.service))
