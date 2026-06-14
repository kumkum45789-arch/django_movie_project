# from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):

    LANGUAGE_CHOICES = [
        ('Hindi', 'Hindi'),
        ('English', 'English'),
    ]

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
    ]

    title = models.CharField(max_length=200)

    rating = models.FloatField()   # 8.5 type values

    popularity = models.IntegerField()  # 0–100 type score

    languages = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='English'
    )

    genres = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        null=True,
        blank=True
    )
    

    def __str__(self):
        return self.title
    