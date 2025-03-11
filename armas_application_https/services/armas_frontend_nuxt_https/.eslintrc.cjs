module.exports = {
    extends: [
      '@nuxtjs',
      'plugin:nuxt/recommended',
      'prettier',
      'plugin:prettier/recommended'
    ],
    plugins: [
      'prettier'
    ],
    // add your custom rules here
    rules: {
      // 'nuxt/no-cjs-in-config': 'off',
    }
  }
  