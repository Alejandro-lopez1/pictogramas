from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.arasaac import ArasaacService


@api_view(["GET"])
def search_pictograms(request):
    word = request.GET.get("q")

    if not word:
        return Response(
            {
                "error": "Missing query parameter q"
            },
            status=400
        )

    pictograms = ArasaacService.search(word)

    return Response(
        {
            "count": len(pictograms),
            "results": pictograms[:10]
        }
    )
