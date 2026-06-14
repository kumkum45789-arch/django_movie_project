# from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from .models import Movie, Language

class MovieTestCase(TestCase):

    def setUp(self):
        lang = Language.objects.create(name="English", code="en")

        Movie.objects.create(
            title="Test Movie",
            rating=8.5,
            popularity=90,
            language=lang
        )

    def test_movie_exists(self):
        movie = Movie.objects.get(title="Test Movie")
        self.assertEqual(movie.rating, 8.5)