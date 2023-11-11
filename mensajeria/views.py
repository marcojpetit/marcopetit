from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mensajeria.models import Mensaje
from django.contrib.auth.models import User


class BandejaDeEntrada(ListView):
    model = Mensaje
    context_object_name = 'listado_de_mensajes_recibidos'
    template_name = 'mensajeria/mensajeria.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(emisor=self.request.user.pk)
        return queryset
class MensajeEnviar(LoginRequiredMixin, CreateView):
    model = Mensaje
    template_name = 'mensajeria/mensaje_enviar.html'
    fields = ['destinatario','contenido']
    
    def form_valid(self, form):
        form.instance.emisor_id = self.request.user.id
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['destinatario'].queryset = User.objects.exclude(pk=self.request.user.pk)
        return form

    def get_success_url(self):
        return reverse_lazy('bandeja_salida')
    
class BandejaDeSalida(ListView):
    model = Mensaje
    context_object_name = 'listado_de_mensajes_enviados'
    template_name = 'mensajeria/bandeja_de_salida.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(destinatario=self.request.user.pk)
        return queryset
        
class DetalleMensaje(DetailView):
    model = Mensaje
    template_name = 'mensajeria/mensaje_detalle.html'

class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Mensaje
    template_name = 'mensajeria/mensaje_eliminar.html'
    success_url = reverse_lazy('mis_mensajes')