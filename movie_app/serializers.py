from jsonschema.exceptions import ValidationError
from rest_framework import serializers
from . import models

class DirectorsListSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Director
        fields = '__all__'

    def get_movies_count(self, obj):
        movies = obj.movies.all()
        return len(movies)

class DirectorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "title director ".split()

class MovieListReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)
    average_review = serializers.SerializerMethodField()
    class Meta:
        model = models.Movie
        fields = "title director reviews average_review".split()

    def get_average_review(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return None
        return sum([review.rating for review in reviews]) / len(reviews)


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class ValidateDirector(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2)


class ValidateMovie(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100, min_length=3)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True, min_value=1)
    director = serializers.PrimaryKeyRelatedField(queryset=models.Director.objects.all())
    reviews = serializers.ListSerializer(child=serializers.CharField(), required=False)


class ValidateReview(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=5)
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)
    movie = serializers.PrimaryKeyRelatedField(queryset=models.Movie.objects.all())
