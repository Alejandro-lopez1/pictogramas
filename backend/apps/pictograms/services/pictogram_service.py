from apps.pictograms.models import Pictogram
from apps.pictograms.serializers import PictogramSerializer


class PictogramService:
    @staticmethod
    def create(data):
        serializer = PictogramSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @staticmethod
    def search(query):
        from .arasaac import ArasaacService

        return ArasaacService.search(query)

    @staticmethod
    def list():
        return Pictogram.objects.all()