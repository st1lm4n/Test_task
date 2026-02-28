from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SlidesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "slides"
    verbose_name = _("Слайды")
