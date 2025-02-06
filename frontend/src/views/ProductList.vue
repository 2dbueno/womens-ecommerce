<template>
  <div class="product-list-page">
    <h1>Produtos</h1>
    
    <!-- Filtros -->
    <div class="filters">
      <label>
        Categoria:
        <select v-model="filters.category">
          <option value="">Todas</option>
          <option v-for="cat in categories" :key="cat.slug" :value="cat.slug">
            {{ cat.name }}
          </option>
        </select>
      </label>
      
      <label>
        Marca:
        <select v-model="filters.brand">
          <option value="">Todas</option>
          <option v-for="brand in brands" :key="brand.slug" :value="brand.slug">
            {{ brand.name }}
          </option>
        </select>
      </label>
      
      <label>
        Cor:
        <input type="text" v-model="filters.color" placeholder="Ex: vermelho" />
      </label>
      
      <label>
        Ordenar por Desconto:
        <select v-model="filters.ordering">
          <option value="-discount">Maior desconto</option>
          <option value="discount">Menor desconto</option>
        </select>
      </label>
      
      <button @click="fetchProducts">Aplicar Filtros</button>
    </div>

    <!-- Lista de Produtos -->
    <div v-if="loading">Carregando produtos...</div>
    <div v-else class="products-grid">
      <div v-if="products.length === 0">Nenhum produto encontrado.</div>
      <div v-for="product in products" :key="product.id" class="product-card">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <p>Preço: R$ {{ product.price }}</p>
        <p>Desconto: {{ product.discount }}%</p>
        <!-- Exiba outras informações relevantes -->
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
      loading: false,
      // Dados fictícios para filtros de categoria e marca; idealmente, esses dados
      // seriam obtidos por meio de endpoints dedicados à listagem de categorias e marcas.
      categories: [
        { name: 'Vestidos', slug: 'vestidos' },
        { name: 'Calças', slug: 'calcas' },
        { name: 'Blusas', slug: 'blusas' },
        { name: 'Acessórios', slug: 'acessorios' },
      ],
      brands: [
        { name: 'Nike', slug: 'nike' },
        { name: 'Gucci', slug: 'gucci' },
        { name: 'Prada', slug: 'prada' },
        { name: 'Balmain', slug: 'balmain' },
      ],
      // Filtros que serão enviados como query parameters
      filters: {
        category: '',
        brand: '',
        color: '',
        ordering: '-discount', // padrão: maior desconto primeiro
      }
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      this.loading = true;
      try {
        // Construa os parâmetros de query dinamicamente com base nos filtros
        const params = {};
        if (this.filters.category) {
          params['category__slug'] = this.filters.category;
        }
        if (this.filters.brand) {
          params['brand__slug'] = this.filters.brand;
        }
        if (this.filters.color) {
          // Aqui usamos o SearchFilter para procurar no array 'color_options'
          params['search'] = this.filters.color;
        }
        if (this.filters.ordering) {
          params['ordering'] = this.filters.ordering;
        }
        const response = await api.get('products/', { params });
        this.products = response.data;
      } catch (error) {
        console.error('Erro ao buscar produtos:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.product-list-page {
  padding: 1rem;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.filters label {
  display: flex;
  flex-direction: column;
  font-weight: bold;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.product-card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
}
</style>
