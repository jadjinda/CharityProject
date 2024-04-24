import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import route from "@/router/route.js";
const app = createApp(App)

app.use(createPinia())
app.use(route)

app.mount('#app')
