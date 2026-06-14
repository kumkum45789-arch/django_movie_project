from rest_framework import serializers
from .models import Movie, Genre, Language

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "rating", "popularity"]