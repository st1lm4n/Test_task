from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class Slide(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    image = FilerImageField(
        on_delete=models.PROTECT, related_name="slides", verbose_name=_("Изображение")
    )
    order = models.PositiveIntegerField(
        default=0, db_index=True, verbose_name=_("Порядок")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))

    class Meta:
        ordering = ["order"]
        verbose_name = _("Слайд")
        verbose_name_plural = _("Слайды")

    def __str__(self) -> str:
        return self.title
