from django.db import models


class Pictogram(models.Model):
    arasaac_id = models.PositiveIntegerField(
        unique=True
    )

    keyword = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True
    )

    image_url = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Pictogram"
        verbose_name_plural = "Pictograms"

    def __str__(self):
        return self.keyword
