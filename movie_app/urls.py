from django.urls import path
from .views import (
    DirectorsListAPIView, DirectorsDetailAPIView,
    MoviesListAPIView, MovieDetailAPIView,
    ReviewsListAPIView, ReviewDetailAPIView
)

urlpatterns = [
    path('directors/', DirectorsListAPIView.as_view(), name='directors_list'),
    path('directors/<int:id>/', DirectorsDetailAPIView.as_view(), name='directors_detail'),
    path('movies/', MoviesListAPIView.as_view(), name='movies_list'),
    path('movies/<int:id>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('reviews/', ReviewsListAPIView.as_view(), name='reviews_list'),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review_detail'),
]
