<template>
  <v-row justify="center">
    <v-col v-if="!loading" cols="12">
      <v-card>
        <v-card-title>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline">
                Titel des Kurses / der Veranstaltung
              </v-list-item-title>
              <v-list-item-subtitle class="subtitle-1">
                Dozent
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card-title>

        <v-divider />

        <v-card-text>
          <v-row justify>
            <v-col cols="12" md="9">
              <v-card>
                <v-card-text>
                  <div
                    style="width: 100%; height: 0px; position: relative; padding-bottom: 56.250%;"
                  >
                    <iframe
                      src="https://www.youtube-nocookie.com/embed/9Iup70E0Ig0"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen
                      width="400"
                      height="300"
                      style="width: 100%; height: 100%; position: absolute;"
                    />
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="3">
              <v-card
                height="100%"
                style="display:flex; flex-direction: column"
              >
                <v-card-text class="grow">
                  Chatnachrichten
                </v-card-text>
                <v-card-actions>
                  <v-row no-gutters>
                    <v-col cols="12">
                      <v-divider class="my-1" />

                      <v-textarea
                        rows="1"
                        outlined
                        filled
                        auto-grow
                        counter
                        placeholder="Chat"
                      >
                      </v-textarea>
                    </v-col>

                    <v-col cols="12">
                      <v-btn color="primary">Senden</v-btn>
                    </v-col>
                  </v-row>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card>
                <v-card-text>
                  Allgemeine Informationen:

                  <ul>
                    <li>ID: {{ courseId }}</li>
                  </ul>
                </v-card-text>
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-expansion-panels focusable accordion multiple>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <span class="subtitle-1">
                      Aufgaben
                    </span>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    Content
                  </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <span class="subtitle-1">
                      Aufzeichnungen
                    </span>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    Content
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>

    <v-progress-circular
      v-else
      :size="70"
      :width="7"
      color="primary"
      indeterminate
    />
  </v-row>
</template>

<script lang="ts">
import { Vue, Watch } from 'vue-property-decorator'
import Component from '~/plugins/vue-class-component'
import { Context } from '@nuxt/types'

@Component
export default class UserOverviewPage extends Vue {
  public loading: boolean = true
  public chatSocket!: WebSocket

  public courseId!: string

  public asyncData(ctx: Context) {}

  public mounted() {
    this.courseId = this.$route.params.id

    const url = 'localhost:3000'
    this.chatSocket = new WebSocket(`wss://${url}/ws/chat/${this.courseId}`)

    this.chatSocket.onmessage = e => {
      const data = JSON.parse(e.data)
      console.log(data)
    }

    this.loading = false
  }
}
</script>
