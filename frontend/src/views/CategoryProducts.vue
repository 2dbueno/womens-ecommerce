<template>
  <div class="category-products-page">
    <h1>Produtos na Categoria: {{ categoryName }}</h1>
    
    <div v-if="loading" class="loading">Carregando produtos...</div>
    
    <div v-else class="products-grid">
      <div v-if="products.length === 0">Nenhum produto encontrado nesta categoria.</div>
      <div v-for="product in products" :key="product.id" class="product-card">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <p>Preço: R$ {{ product.price }}</p>
        <p>Desconto: {{ product.discount }}%</p>
        <!-- Você pode incluir outros detalhes do produto, como imagens, botão de compra, etc. -->
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'CategoryProducts',
  data() {
    return {
      products: [],
      loading: false,
      categoryName: '',
    };
  },
  mounted() {
    this.fetchCategoryProducts();
  },
  methods: {
    async fetchCategoryProducts() {
      this.loading = true;
      try {
        // Obtém o slug da categoria a partir dos parâmetros da rota
        const categorySlug = this.$route.params.slug;
        
        // Define um nome de exibição para a categoria (pode ser aprimorado conforme necessidade)
        this.categoryName = categorySlug.charAt(0).toUpperCase() + categorySlug.slice(1);
        
        // Faz a requisição para o endpoint de produtos, filtrando pela categoria
        const response = await api.get('products/', {
          params: { 'category__slug': categorySlug }
        });
        this.products = response.data;
      } catch (error) {
        console.error('Erro ao buscar produtos da categoria:', error);
      } finally {
        this.loading = false;
      }
    }
  },
  watch: {
    // Se o slug da categoria mudar, recarrega os produtos
    '$route.params.slug': 'fetchCategoryProducts'
  }
};
</script>

<style scoped>
.category-products-page {
  padding: 1rem;
}

.loading {
  font-size: 1.2rem;
  text-align: center;
  padding: 2rem;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.product-card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  transition: box-shadow 0.3s ease;
}

.product-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
