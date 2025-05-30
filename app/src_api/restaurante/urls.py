from rest_framework.routers import DefaultRouter
from django.urls import path, include
from restaurante.views import (IngredienteServices, CardapioService,
                               AutenticacaoServices, EmpregadoService, CategoriaServices, 
                               MesaServices, ComandaServices, ClienteService, FormaPagamentoServices,
                               PedidoServices, ItemPedidoServices, EstoqueServices)

router = DefaultRouter()
router.register(r'cardapio', CardapioService, basename='cardapio')
router.register(r'usuario', AutenticacaoServices, basename='usuario')
router.register(r'empregado', EmpregadoService, basename='empregado')
router.register(r'categoria', CategoriaServices, basename='categoria')
router.register(r'mesa', MesaServices, basename='mesa')
router.register(r'comanda', ComandaServices, basename='comanda')
router.register(r'cliente', ClienteService, basename='cliente')
router.register(r'forma-pagamento', FormaPagamentoServices, basename='forma-pagamento')
router.register(r'ingrediente', IngredienteServices, basename='ingrediente')
router.register(r'pedido', PedidoServices, basename='pedido')
router.register(r'itempedido', ItemPedidoServices, basename='itempedido')
router.register(r'estoque', EstoqueServices, basename='estoque')

urlpatterns = [
    path('api/', include(router.urls)),  # Todas as rotas dentro de /api/
]




