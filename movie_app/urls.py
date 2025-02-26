from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.directors_list_api_view),
    path('directors/<int:id>/', views.directors_detail_api_view),

    path('/movies/', views.movies_list_api_view),
    path('/movies/<int:id>/', views.movie_detail_api_view),

    path('/reviews/', views.reviews_list_api_view),
    path('/reviews/<int:id>/', views.reviews_detail_api_view),

]
