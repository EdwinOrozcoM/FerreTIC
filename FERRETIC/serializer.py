from rest_framework import serializers
from FERRETIC.models import *

class Empleado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Sucursal_serializer(serializers.ModelSerializer):
    empleado = Empleado_serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(),source='empleado')
    class Meta:
        model = Sucursal
        fields = '__all__'

class Proveedor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class Factura_serializer(serializers.ModelSerializer):
    cliente = Cliente_serializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cliente.objects.all(),source='cliente')
    empleado = Empleado_serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(),source='empleado')
    class Meta:
        model = Factura
        fields = '__all__'

class Producto_serializer(serializers.ModelSerializer):
    proveedor = Proveedor_serializer(read_only=True)
    proveedor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proveedor.objects.all(),source='proveedor')
    class Meta:
        model = Producto
        fields = '__all__'

class Factura_Producto_serializer(serializers.ModelSerializer):
    factura = Factura_serializer(read_only=True)
    factura_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Factura.objects.all(),source='factura')
    producto = Producto_serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(),source='producto')
    class Meta:
        model = Factura_Producto
        fields = '__all__'

class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario(
            Username=validated_data['Username'],
            Correo=validated_data['Correo'],
            Telefono=validated_data['Telefono'],
            Nombre=validated_data['Nombre'],
        )
        user.set_password(validated_data['Password'])
        user.save()
        return user