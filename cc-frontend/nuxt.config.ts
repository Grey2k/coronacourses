import dotenv from 'dotenv'
import VuetifyLoaderPlugin from 'vuetify-loader/lib/plugin'

dotenv.config()

const sassLoaderOptions = {
  implementation: require('sass'),
}

export default {
  dev: process.env.NODE_ENV !== 'production',

  // env: {
  //   apiUrl: process.env.API_URL || '',
  // },

  server: {
    host: process.env.HOST || '0.0.0.0',
    port: process.env.HOST_PORT || 3000,
  },

  buildModules: ['@nuxt/typescript-build'],

  watch: ['./graphql/**/*.ts'],

  serverMiddleware: [{path: '/ping', handler: '~/api/healthcheck.js'}],

  build: {
    plugins: [new VuetifyLoaderPlugin()],
    transpile: [/^vuetify/],
    loaders: {
      scss: sassLoaderOptions,
      sass: sassLoaderOptions,
    },
    // Transform asset urls for v-img.
    extend(webpackConfig, {isDev, isClient, loaders: {vue}}) {
      // Produce source maps in dev mode for debugging.
      if (isDev) {
        webpackConfig.devtool = 'source-map'
      }

      // Extend only webpack config for client-bundle
      if (isClient) {
        vue.transformAssetUrls['v-img'] = ['src']
      }
    },
  },

  // https://vuetifyjs.com/en/guides/a-la-carte
  // Vuetify main styles.
  css: [
    'vuetify/src/styles/main.sass',
    '~/assets/scrollbar.sass',
  ],

  plugins: [
    '~/plugins/vuetify.ts',
  ],

  modules: [
    // 'cookie-universal-nuxt',
    // '@nuxtjs/sitemap',
  ],

  // sitemap: {
  //   hostname: 'https://egm-development.com',
  //   gzip: true,
  //   cacheTime: 1000 * 60 * 15,
  //   path: '/getsitemap.xml',
  //   exclude: ['/de/**', '/intern/**', '/client/me', '/client/download'],
  //   routes: ['/index', '/changelog', '/intern/login'],
  // },

  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {},

  head: {
    meta: [
      {
        name: 'viewport',
        content:
            'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no',
      },
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
      {
        rel: 'stylesheet',
        href:
            'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons',
      },
    ],

  }
}