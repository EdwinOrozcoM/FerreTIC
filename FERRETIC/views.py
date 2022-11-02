import datetime
from FERRETIC.models import *
from FERRETIC.serializer import *
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class TokenProvider(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.Token = token.key
        user.save()
        usuario = Usuario_serializer(user)
        return Response(usuario.data)

class Empleado_view(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = Empleado_serializer

class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer

class Sucursal_view(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = Cliente_serializer

class Proveedor_view(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = Proveedor_serializer

class Factura_view(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = Factura_serializer

class Producto_view(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer
#No deviera manipularla ya que es una relacion de many a many
class Factura_Producto_view(viewsets.ModelViewSet):
    queryset = Factura_Producto.objects.all()
    serializer_class = Factura_Producto_serializer

class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializer

