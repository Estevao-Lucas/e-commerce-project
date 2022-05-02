from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from .models import Produto

# Create your views here.
class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10

class DetalheProduto(View):
    pass

class AddCarrinho(View):
    pass

class RmCarrinho(View):
    pass

class Finalizar(View):
    pass

class Carrinho(View):
    pass