from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ComandaViewSet, FormaPagamentoViewSet,
    PedidoViewSet, CategoriaViewSet, MenuViewSet, ItemMenuViewSet, ClienteViewSet
)

router = DefaultRouter()
router.register(r'comandas', ComandaViewSet)
router.register(r'formas-pagamento', FormaPagamentoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'itens-menu', ItemMenuViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

