from django.urls import path
from .views import AuthorizationAPIView, RegistrationAPIView, ConfirmRegistrationAPIView

urlpatterns = [
    path('authorization/', AuthorizationAPIView.as_view(), name='authorization'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('confirm-registration/', ConfirmRegistrationAPIView.as_view(), name='confirm_registration'),
]
