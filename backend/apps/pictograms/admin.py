from django.contrib import admin

from .models import Pictogram


@admin.register(Pictogram)
class PictogramAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "arasaac_id",
        "keyword",
        "created_at",
    )

    search_fields = (
        "keyword",
    )
