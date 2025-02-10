from django.contrib import admin
from django.urls import path
from movie_app import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_api_view),
    path('api/v1/directors/<int:id>/', views.directors_detail_api_view),
    path('api/v1/movies/', views.movies_list_api_view),
    path('api/v1/movies/reviews/', views.movies_reviews_list_api_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_api_view),

]
