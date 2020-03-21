<template>
  <v-app app>
    <v-navigation-drawer app :value="navbarVisible" fixed width="300px">
      <strong class="display-1 primary--text">
        CoronaCourses
      </strong>

      <v-divider />

      <v-list dense>
        <v-list-item nuxt :to="'/'">
          <v-list-item-action>
            <v-icon small>fa-home</v-icon>
          </v-list-item-action>
          <v-list-item-title class="font-weight-regular">
            Startseite
          </v-list-item-title>
        </v-list-item>

        <v-list-item nuxt :to="'/courses'">
          <v-list-item-action>
            <v-icon small>fa-book</v-icon>
          </v-list-item-action>
          <v-list-item-title class="font-weight-regular">
            Kurse
          </v-list-item-title>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-subheader>
        <strong>
          > Hinweise <
        </strong>
      </v-subheader>
    </v-navigation-drawer>

    <nav>
      <v-app-bar app dark color="primary">
        <v-app-bar-nav-icon @click="drawer" />

        <v-spacer />

        <v-toolbar-items>
          <v-menu
            offset-y
            :close-on-content-click="false"
            transition="slide-x-transition"
          >
            <template v-slot:activator="{ on }">
              <v-btn text v-on="on">
                <v-icon small>fa-ellipsis-v</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-switch
                  v-model="$vuetify.theme.dark"
                  label="Darkmode"
                  @change="updateDarkModeCookie()"
                ></v-switch>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar-items>
      </v-app-bar>
    </nav>

    <notification />

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>
<script lang="ts">
import { State } from 'vuex-class'
import { Vue } from 'vue-property-decorator'
import { DateTime } from 'luxon'
import Component from '~/plugins/vue-class-component'
import notification from '~/components/notification.vue'

@Component({
  components: {
    // cookieAcceptor,
    notification,
  },
  // middleware: 'tosAndEmailCheck',
})
export default class DefaultLayout extends Vue {
  public navbarVisible: boolean | null = null
  public copyrightNotice: string = ''

  @State me

  async mounted() {
    // eslint-disable-next-line no-unused-expressions
    // this.me
  }

  drawer() {
    if (this.navbarVisible === null) {
      this.navbarVisible = window.innerWidth < 1264
      return
    }

    if (window.innerWidth < 1264) {
      this.navbarVisible = false
      setTimeout(() => {
        this.navbarVisible = true
      }, 0)
      return
    }

    this.navbarVisible = !this.navbarVisible
  }

  public async logout() {
    // await this.$store!.dispatch('logout')
  }

  public updateDarkModeCookie() {
    document.cookie = `dark-mode=${this.$vuetify.theme.dark.toString()}; path=/`
  }
}
</script>

<style scoped>
a {
  color: var(--v-link-base);
  text-decoration: none;
}
</style>
