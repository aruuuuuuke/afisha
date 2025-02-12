from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status



@api_view(http_method_names=['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        data = serializers.DirectorsListSerializer(instance=directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(data=serializers.DirectorsDetailSerializer(instance=director).data,
                        status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def directors_detail_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = serializers.DirectorsDetailSerializer(instance=director).data
        return Response(data=data)

    elif request.method == 'PUT':
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=serializers.DirectorsDetailSerializer(instance=director).data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializers.MovieListSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director')
        movie = models.Movie.objects.create(
            title=title,
            description=description,
            duration=int(duration),
            director_id=director_id
        )
    return Response(data=serializers.MovieDetailSerializer(instance=movie).data,
                    status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET'])
def movies_reviews_list_api_view(request):
    movies = models.Movie.objects.all()
    data = serializers.MovieListReviewsSerializer(instance = movies, many=True).data
    return Response(data = data)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(instance=movie).data
        return Response(data=data)

    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director')

        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director = models.Director.objects.get(id=director_id)
        movie.save()
        return Response(data=serializers.MovieDetailSerializer(instance=movie).data)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        data = serializers.ReviewListSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        rating = request.data.get('rating')
        movie_id = request.data.get('movie')
        movie = models.Movie.objects.get(id=movie_id)
        review = models.Review.objects.create(
            text=text,
            rating=int(rating),
            movie_id=movie_id
        )
        return Response(data=serializers.ReviewDetailSerializer(instance=review).data,
                        status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = serializers.ReviewDetailSerializer(instance=review, many=False).data
        return Response(data=data)

    elif request.method == 'PUT':
        text = request.data.get('text')
        rating = request.data.get('rating')
        review.text = text
        review.rating = rating
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(instance=review).data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
