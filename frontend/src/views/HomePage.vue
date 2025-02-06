<template>
  <div class="home-page">
    <!-- Seção Hero -->
    <section class="hero">
      <div class="hero-background"></div>
      <div class="hero-content">
        <h1>Bem-vinda ao Nosso E-commerce</h1>
        <p>Descubra as últimas tendências em moda feminina</p>
      </div>
    </section>

    <!-- Seção de Categorias -->
    <section class="categories">
      <h2>Categorias</h2>
      <div class="categories-grid">
        <!-- Itera sobre as categorias definidas no data() -->
        <div 
          class="category-card" 
          v-for="category in categories" 
          :key="category.id"
        >
          <!-- O título da categoria é clicável e redireciona para a página da categoria -->
          <router-link :to="`/category/${category.slug}`">
            <img 
              :src="category.image" 
              :alt="category.title" 
              class="category-image"
            />
            <div class="category-title">{{ category.title }}</div>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      // Exemplo de categorias – essas informações podem vir de uma API ou do banco de dados
      categories: [
        {
          id: 1,
          title: 'Acessórios',
          slug: 'acessorios',
          image: require('@/assets/images/categories/accessories-category.jpg'),
        },
        {
          id: 2,
          title: 'Vestidos',
          slug: 'vestidos',
          image: require('@/assets/images/categories/dresses-category.jpg'),
        },
        {
          id: 3,
          title: 'Calças',
          slug: 'calcas',
          image: require('@/assets/images/categories/pants-category.jpg'),
        },
        {
          id: 4,
          title: 'Blusas',
          slug: 'blusas',
          image: require('@/assets/images/categories/tops-category.jpg'),
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Container principal da HomePage */
.home-page {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Seção Hero */
.hero {
  position: relative;
  width: 100%;
  height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/images/background-home.jpg');
  background-size: cover;
  background-position: center;
  filter: brightness(0.7);
  z-index: -1;
}

.hero-content {
  text-align: center;
  color: #FFF;
  z-index: 1;
}

.hero-content h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: var(--color-primary-1000);
}

.hero-content p {
  font-size: 1.5rem;
}

/* Seção de Categorias */
.categories {
  padding: 2rem;
}

.categories h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: var(--color-primary-500);
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  padding: 0 1rem;
}

.category-card {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.category-card:hover {
  transform: scale(1.03);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.category-card img {
  width: 100%;
  display: block;
  transition: transform 0.3s ease;
}

.category-card:hover img {
  transform: scale(1.1);
}

.category-title {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  color: #FFF;
  text-align: center;
  padding: 0.5rem 0;
  font-size: 1.2rem;
  text-transform: uppercase;
  transition: background-color 0.3s ease;
}

.category-card:hover .category-title {
  background-color: rgba(0, 0, 0, 0.7);
}
</style>
