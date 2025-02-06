import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Importa o arquivo global de variáveis
import './assets/css/variables.css';

const app = createApp(App);

app.use(router);

app.mount('#app');
