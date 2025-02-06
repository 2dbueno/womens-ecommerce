from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from products.views import ProductViewSet
from cart.views import CartDetail, AddCartItem
from accounts.views import UserRegisterView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

# Cria um roteador para o Django REST Framework e registra o ViewSet dos produtos
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    # Rota para a área administrativa do Django
    path('admin/', admin.site.urls),
    
    # Inclui as rotas geradas pelo router (no caso, para os produtos)
    path('api/', include(router.urls)),
    
    # Endpoints customizados para o carrinho
    path('api/cart/', CartDetail.as_view(), name='cart-detail'),
    path('api/cart/add/', AddCartItem.as_view(), name='cart-add'),
    
    # Endpoint para registro de usuários
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    
    # Endpoints para autenticação com JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
