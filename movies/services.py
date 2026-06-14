from .models import Movie, Genre

class MovieService:

    @staticmethod
    def get_movies(genres=None, languages=None):
        qs = Movie.objects.all()

        if languages:
            qs = qs.filter(language__code__in=languages)

        if genres:
            qs = qs.filter(genres__id__in=genres).distinct()

        return qs

    @staticmethod
    def get_facets():
        return Genre.objects.all()