import requests


class ArasaacService:
    BASE_URL = "https://api.arasaac.org/api/pictograms"

    @classmethod
    def search(cls, word: str, locale: str = "es") -> list:
        url = f"{cls.BASE_URL}/{locale}/search/{word}"

        try:
            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException:
            return []
