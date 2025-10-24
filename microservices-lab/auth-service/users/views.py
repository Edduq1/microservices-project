from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import serializers

User = get_user_model()

# SERIALIZER PARA REGISTRO (SOLO ESCRITURA)
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}} # Oculta el password

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# SERIALIZER PARA MOSTRAR DATOS (SOLO LECTURA)
class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email') # <-- Solo expone campos seguros


# VISTAS (VIEWS)
# Vista para /api/register/
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer # <-- Usa el serializer de REGISTRO

# Vista para /api/me/ (La versión correcta)
class MeView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserDisplaySerializer # <-- Usa el serializer de LECTURA

    def get_object(self):
        return self.request.user