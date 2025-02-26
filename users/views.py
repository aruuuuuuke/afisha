from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import serializers, models
import random

@api_view(['POST'])
def authorization_api_view(request):
    serializer = serializers.AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def registration_api_view(request):
    serializer = serializers.RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username=username,
                                    password=password,
                                    is_active=False)

    confirmation_code = models.ConfirmationCode.objects.create(user=user, code=str(random.randint(100000, 999999)))

    return Response({'message': 'User registered successfully. Please confirm your registration.',
                     'confirmation_code': confirmation_code.code},
                    status=status.HTTP_201_CREATED)

@api_view(['POST'])
def confirm_registration_api_view(request):
    code = request.data.get('code')
    try:
        confirmation_code = models.ConfirmationCode.objects.get(code=code)
    except models.ConfirmationCode.DoesNotExist:
        return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)

    if not confirmation_code.is_confirmed:
        confirmation_code.is_confirmed = True
        confirmation_code.user.is_active = True
        confirmation_code.user.save()
        confirmation_code.save()
        return Response({'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)

    return Response({'error': 'Code already used or user already confirmed'}, status=status.HTTP_400_BAD_REQUEST)


