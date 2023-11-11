from django.urls import path
from mensajeria.views import BandejaDeEntrada, MensajeEnviar, BandejaDeSalida, DetalleMensaje, EliminarMensaje

urlpatterns = [
    path('', BandejaDeEntrada.as_view(), name='mis_mensajes'),
    path('enviar/', MensajeEnviar.as_view(), name='mensaje_enviar'),
    path('bandeja_salida/', BandejaDeSalida.as_view(), name='bandeja_salida'),
    path('mensaje/<int:pk>', DetalleMensaje.as_view(), name='detalle_mensaje'),
    path('eliminar/<int:pk>', EliminarMensaje.as_view(), name='mensaje_eliminar'),
    ]