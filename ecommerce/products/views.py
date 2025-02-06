from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar, filtrar e editar produtos.
    
    Funcionalidades de filtro e ordenação:
      - Filtra por categoria utilizando o campo 'category__slug'
      - Filtra por marca utilizando o campo 'brand__slug'
      - Permite buscar por uma determinada opção de cor (usando o campo 'color_options' como texto)
      - Ordena os produtos pelo campo 'discount' (desconto), com ordenação padrão do maior para o menor
    """
    # Recupera somente os produtos disponíveis
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

    # Configura os backends de filtro, busca e ordenação
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define quais campos podem ser filtrados diretamente via query parameters:
    # Exemplo: ?category__slug=vestidos, ?brand__slug=nike
    filterset_fields = {
        'category__slug': ['exact'],
        'brand__slug': ['exact'],
    }

    # Para filtrar por opções de cor, utilizamos o SearchFilter.
    # Exemplo: ?search=vermelho (vai procurar no array 'color_options')
    search_fields = ['color_options']

    # Permite ordenar pelo percentual de desconto
    ordering_fields = ['discount']
    ordering = ['-discount']  # Ordenação padrão: maior desconto primeiro
