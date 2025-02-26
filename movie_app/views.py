from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class DirectorsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        directors = models.Director.objects.all()
        data = serializers.DirectorsListSerializer(instance=directors, many=True).data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.ValidateDirector(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data['name']
        director = models.Director.objects.create(name=name)
        return Response(data=serializers.DirectorsDetailSerializer(instance=director).data,
                        status=status.HTTP_201_CREATED)


class DirectorsDetailAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            director = models.Director.objects.get(id=id)
        except models.Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = serializers.DirectorsDetailSerializer(instance=director).data
        return Response(data=data)

    def put(self, request, id, *args, **kwargs):
        try:
            director = models.Director.objects.get(id=id)
        except models.Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ValidateDirector(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        director.name = serializer.validated_data['name']
        director.save()
        return Response(data=serializers.DirectorsDetailSerializer(instance=director).data)

    def delete(self, request, id, *args, **kwargs):
        try:
            director = models.Director.objects.get(id=id)
        except models.Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        movies = models.Movie.objects.all()
        data = serializers.MovieListSerializer(instance=movies, many=True).data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
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


class MovieDetailAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            movie = models.Movie.objects.get(id=id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = serializers.MovieDetailSerializer(instance=movie).data
        return Response(data=data)

    def put(self, request, id, *args, **kwargs):
        try:
            movie = models.Movie.objects.get(id=id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ValidateMovie(data=request.data)
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

    def delete(self, request, id, *args, **kwargs):
        try:
            movie = models.Movie.objects.get(id=id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        reviews = models.Review.objects.all()
        data = serializers.ReviewListSerializer(instance=reviews, many=True).data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
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


class ReviewDetailAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            review = models.Review.objects.get(id=id)
        except models.Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = serializers.ReviewDetailSerializer(instance=review).data
        return Response(data=data)

    def put(self, request, id, *args, **kwargs):
        try:
            review = models.Review.objects.get(id=id)
        except models.Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ValidateReview(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        text = serializer.validated_data.get('text', review.text)
        rating = serializer.validated_data.get('rating', review.rating)
        review.text = text
        review.rating = rating
        review.save()
        return Response(data=serializers.ReviewDetailSerializer(instance=review).data)

    def delete(self, request, id, *args, **kwargs):
        try:
            review = models.Review.objects.get(id=id)
        except models.Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
