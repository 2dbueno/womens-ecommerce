<template>
  <nav class="navbar">
    <div class="container">
      <router-link to="/" class="logo">Meu E-commerce</router-link>
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/products">Produtos</router-link></li>
        <!-- Adicione outros links conforme necessário -->
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppNavbar'
};
</script>

<style scoped>
.navbar {
  background-color: var(--color-primary-500);
  padding: 1rem;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
}
.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}
.nav-links a {
  color: #FFF;
  text-decoration: none;
}
.logo {
  font-weight: bold;
  color: #FFF;
  text-decoration: none;
}
</style>
