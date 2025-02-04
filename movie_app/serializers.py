from rest_framework import serializers
from . import models

class DirectorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'

class DirectorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "title director".split()

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'