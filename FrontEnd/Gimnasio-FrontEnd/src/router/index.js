import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterUser from '@/components/RegisterUser.vue'
import  Home from '@/components/Home.vue'
import Menu from '@/components/Menu.vue'
import Persona from '@/components/Persona.vue'
import Dashboard from '@/components/Dashboard.vue'
import Miembros from '@/components/Miembros.vue'
import Membresias from '@/components/Membresias.vue'
import TransaccionPagos from '@/components/TransaccionPagos.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser
    },
    {
      path: '/home',
      name: 'home',
      component: Menu,
      children: [
        {path: '/personas', name: 'personas', component: Persona},
        {path: '/dashboard', name: 'dashboard', component: Dashboard},
        {path: '/miembros', name: 'miembros', component: Miembros},
        {path: '/membresias', name: 'membresias', component: Membresias},
        {path: '/transaccion-pagos', name: 'transaccionPagos', component: TransaccionPagos},
      ]
    }
  ]
})

export default router
