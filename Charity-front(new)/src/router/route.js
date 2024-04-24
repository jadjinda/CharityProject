import { createRouter, createWebHistory } from 'vue-router'

import App from '@/App.vue'
import Categorie from '@/components/Categorie.vue'
import Projet from '@/components/Projet.vue'

const route = createRouter({
  history: createWebHistory(),
  routes: [
      {
        path:'/',
        name: 'home',
        component: App
      },
      {
      path: '/categorie',
      name: 'categorie',
      component: Categorie
      },
      {
      path: '/projet',
      name: 'projet',
      component: Projet
      },
  ]
})

export default route