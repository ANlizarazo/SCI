from django.forms import ModelForm
from compras.models import  DetalleCompra

"""class CompraUpdateForm(ModelForm):
    class Meta:
        model= Compra
        exclude=['estado']"""

class DetalleCompraForm(ModelForm):
    class Meta:
        model= DetalleCompra
        fields = ['proveedor', 'producto','cantidadProducto','valorUnidad','totalCompra']
