import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import de from 'vuetify/src/locale/de'
import colors from 'vuetify/lib/util/colors'
import { Context } from '@nuxt/types'
// eslint-disable-next-line import/no-extraneous-dependencies
import '@fortawesome/fontawesome-free/css/all.css'

// https://vuetifyjs.com/en/style/theme
// const LRU = require('lru-cache')
import LRU from 'lru-cache'

const themeCache = new LRU({
  max: 10,
  maxAge: 1000 * 60 * 60 // 1 hour
})

Vue.use(Vuetify)

export default (ctx: Context) => {
  let darkModeEnabled = false
  const cookies = process.client ? document.cookie : ctx.req.headers.cookie

  if (cookies !== undefined) {
    const darkModeCookie = cookies
      .split('; ')
      .find((cookie) => cookie.split('=')[0] === 'dark-mode')

    if (darkModeCookie && darkModeCookie.split('=')[1] === 'false') {
      darkModeEnabled = false
    }
  }

  ctx.app.vuetify = new Vuetify({
    lang: {
      locales: { de },
      current: 'de'
    },
    icons: {
      iconfont: 'fa'
    },
    theme: {
      dark: darkModeEnabled,
      themes: {
        dark: {
          primary: colors.blue.base,
          secondary: colors.grey.base,
          accent: colors.orange.accent4,
          error: colors.red.darken2,
          warning: colors.orange.accent3,
          info: colors.lightBlue.darken2,
          success: colors.green.accent4,
          link: colors.red.lighten1
        },
        light: {
          primary: colors.blue.base,
          secondary: colors.grey.base,
          accent: colors.orange.accent4,
          error: colors.red.darken2,
          warning: colors.orange.accent3,
          info: colors.lightBlue.darken2,
          success: colors.green.accent4,
          link: colors.red.lighten1
        }
      },
      options: {
        themeCache,
        minifyTheme: (css: string) => {
          return process.env.NODE_ENV === 'production'
            ? css.replace(/[\r\n|\r|\n]/g, '')
            : css
        },
        customProperties: true
      }
    }
  })
}
