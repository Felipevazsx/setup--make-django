
from django.views.generic.edit import FormView
from .forms import FormularioTeste
import requests

class FormularioView(FormView):
    template_name = 'formulario.html'
    form_class = FormularioTeste
    success_url = '/sucesso/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        # Enviar os dados para o webhook do Make
        response = requests.post(
            'https://hook.us2.make.com/o4u1dywzdg6mkwh15xhywtozpu3gc6wl',  # Substitua pela URL do seu webhook Make
            data=form_data
        )
        print(response.text)
        return super().form_valid(form)
