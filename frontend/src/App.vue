<template>
  <div id="app">
    <!-- Renderiza a Navbar se a rota não tiver meta 'hideNavbar' -->
    <AppNavbar v-if="!$route.meta.hideNavbar" />
    <div class="content" :class="{'with-navbar': !$route.meta.hideNavbar}">
      <router-view />
    </div>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue';

export default {
  name: 'App',
  components: {
    AppNavbar
  }
};
</script>

<style>
/* Ajuste para não ficar oculto atrás da navbar fixa */
.content.with-navbar {
  padding-top: 70px; /* ajuste conforme a altura da Navbar */
}
</style>
