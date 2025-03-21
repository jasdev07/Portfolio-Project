// File: middleware/redirect.js

export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path === '/') {
    return navigateTo('/');
  }
});
