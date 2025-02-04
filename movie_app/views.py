from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status

# Create your views here.
@api_view(http_method_names=['GET'])
def directors_list_api_view(request):
    directors = models.Director.objects.all()
    data = serializers.DirectorsListSerializer(instance = directors, many=True).data
    return Response(data = data)

@api_view(http_method_names=['GET'])
def directors_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id = id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.DirectorsDetailSerializer(instance = director, many=False).data
    return Response(data = data)


@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
    movies = models.Movie.objects.all()
    data = serializers.MovieListSerializer(instance = movies, many=True).data
    return Response(data = data)

@api_view(http_method_names=['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id = id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.MovieDetailSerializer(instance = movie, many=False).data
    return Response(data = data)

@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = models.Review.objects.all()
    data = serializers.ReviewListSerializer(instance = reviews, many=True).data
    return Response(data = data)

@api_view(http_method_names=['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id = id)
    except models.Review.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    data = serializers.ReviewDetailSerializer(instance = review, many=False).data
    return Response(data = data)