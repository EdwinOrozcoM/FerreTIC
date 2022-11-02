
from django.urls import path, include
from FERRETIC.views import *
from rest_framework import routers
router =routers.DefaultRouter()
router.register('empleado',Empleado_view,basename='empleado')
router.register('usuario',Usuario_view,basename='usuario')
router.register('cliente',Cliente_view,basename='cliente')
router.register('sucursal',Sucursal_view,basename='sucursal')
router.register('proveedor',Proveedor_view,basename='proveedor')
router.register('factura',Factura_view,basename='factura')
router.register('producto',Producto_view,basename='producto')

urlpatterns = [
       path('', include(router.urls)),
       path('Token',TokenProvider.as_view(),name='token'),
]
