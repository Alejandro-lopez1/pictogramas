from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import PictogramSerializer
from .services.pictogram_service import PictogramService


@api_view(["GET"])
def search_pictograms(request):
    query = request.GET.get("q")

    if not query:
        return Response(
            {"error": "Missing query parameter q"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    results = PictogramService.search(query)

    return Response(
        {
            "count": len(results),
            "results": results[:10],
        }
    )


@api_view(["POST"])
def create_pictogram(request):
    try:
        pictogram = PictogramService.create(request.data)

        serializer = PictogramSerializer(pictogram)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    except ValidationError as exc:
        return Response(
            exc.detail,
            status=status.HTTP_400_BAD_REQUEST,
        )