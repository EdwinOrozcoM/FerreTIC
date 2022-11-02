from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Empleado(models.Model):
    Documento= models.CharField(max_length=25, unique=True)
    Nombre= models.CharField(max_length=45)
    Username= models.CharField(max_length=32)
    Direccion= models.CharField(max_length=55)
    Telefono= models.CharField(max_length=10)
    Fecha_nacimiento= models.DateTimeField(auto_now=False)
    Correo= models.CharField(max_length=50)
    #token= models.CharField(max_length=100,null=True,blank=True,default='')
    Tipo_empleado= models.CharField(max_length=25)

    def __str__(self):
        return self.Nombre

class Usuario(AbstractUser):
    Nombre = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)
    Token = models.CharField(max_length=100, null=True,blank=True,default='')

class Cliente(models.Model):
    Nombre = models.CharField(max_length=45)
    Documento= models.CharField(max_length=25, unique=True)
    Direccion= models.CharField(max_length=55)
    Telefono= models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Sucursal(models.Model):
    Nombre = models.CharField(max_length=30)
    Codigo = models.CharField(max_length=25)
    Dirreccion = models.CharField(max_length=55)
    Empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return self.Nombre

class Proveedor(models.Model):
    Codigo= models.CharField(max_length=20)
    Nombre= models.CharField(max_length=25)
    Estado= models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre


class Factura(models.Model):
    Numero = models.CharField(max_length=15)
    Fecha_venta= models.DateTimeField(auto_now=False)
    Valor= models.IntegerField()
    Cantidad= models.IntegerField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    Empleado= models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return 'Numero de Factura : '+self.Numero+' compra de '+self.Cliente.Nombre

class Producto(models.Model):
    Codigo = models.CharField(max_length=20)
    Nombre= models.CharField(max_length=25)
    Costo= models.IntegerField()
    Precio_venta= models.IntegerField()
    Linea_produto= models.CharField(max_length=20)
    Fecha_compra = models.DateTimeField(auto_now=False)
    Marca = models.CharField(max_length=21)
    Proveedor = models.ForeignKey(Proveedor,on_delete=models.PROTECT)

    def __str__(self):
        return self.Codigo+' del  producto: '+self.Nombre

class Factura_Producto(models.Model):
    Factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    Producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    def __str__(self):
        return self.Factura.Numero+''+self.Producto.Nombre



