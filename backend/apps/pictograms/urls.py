from django.urls import path

from . import views

urlpatterns = [
    path(
        "search/",
        views.search_pictograms,
        name="search-pictograms",
    ),
    path(
        "",
        views.create_pictogram,
        name="create-pictogram",
    ),
]

