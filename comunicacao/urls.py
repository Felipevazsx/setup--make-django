from django.urls import path
from .views import FormularioView
from django.views.generic import TemplateView

urlpatterns = [
    path('', FormularioView.as_view(), name='formulario'),
    path('sucesso/', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
]
