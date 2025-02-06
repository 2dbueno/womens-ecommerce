import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/HomePage.vue';
import ProductList from '@/views/ProductList.vue';
import ShoppingCart from '@/views/ShoppingCart.vue';
import CheckoutPage from '@/views/CheckoutPage.vue';
import CategoryProducts from '@/views/CategoryProducts.vue'; // Importa o componente

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/products',
    name: 'Products',
    component: ProductList
  },
  {
    path: '/cart',
    name: 'Cart',
    component: ShoppingCart,
    meta: { hideNavbar: true }
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: CheckoutPage,
    meta: { hideNavbar: true }
  },
  {
    path: '/category/:slug',
    name: 'CategoryProducts',
    component: CategoryProducts,
  },
  // Outras rotas, como login, registro, etc.
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
