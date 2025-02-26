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
        serializer = serializers.ValidateDirector(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data['name']
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
        serializer = serializers.ValidateDirector(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        director.name = serializer.validated_data['name']
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
        serializer = serializers.ValidateMovie(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data['title']
        description = serializer.validated_data.get('description', '')
        duration = serializer.validated_data['duration']
        director_id = serializer.validated_data['director']

        movie = models.Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )

        return Response(data=serializers.MovieDetailSerializer(instance=movie).data,
                        status=status.HTTP_201_CREATED)


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
        serializer = serializers.ValidateMovie(data=request.data)  # Changed to ValidateMovie
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('title', movie.title)
        description = serializer.validated_data.get('description', movie.description)
        duration = serializer.validated_data.get('duration', movie.duration)
        director_id = serializer.validated_data.get('director', movie.director.id)

        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director = models.Director.objects.get(id=director_id)
        movie.save()
        return Response(data=serializers.MovieDetailSerializer(instance=movie).data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        data = serializers.ReviewListSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = serializers.ValidateReview(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        text = serializer.validated_data['text']
        rating = serializer.validated_data['rating']
        movie_id = serializer.validated_data['movie']
        review = models.Review.objects.create(
            text=text,
            rating=rating,
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
        data = serializers.ReviewDetailSerializer(instance=review).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = serializers.ValidateReview(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        text = serializer.validated_data.get('text', review.text)
        rating = serializer.validated_data.get('rating', review.rating)
        review.text = text
        review.rating = rating
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(instance=review).data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
