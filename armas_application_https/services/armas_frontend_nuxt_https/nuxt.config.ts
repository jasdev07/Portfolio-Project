// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: false },
  css: ['~/assets/css/tailwind.css',
        '~/assets/css/transitions.css'
      ], 
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],
  app: {
    baseURL: '/d/armas/',
    head: {
      link: [
        { rel: 'icon', type: 'image/png', href: '/armas.png' }
      ]
    }
  },
  runtimeConfig: {
    public: {
      backendApiUrl: process.env.BACKEND_API_URL,

    },
  },
  



});
