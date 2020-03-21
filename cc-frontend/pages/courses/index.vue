<template>
  <v-row justify="center">
    <v-col v-if="!loading" cols="12">
      <v-row>
        <v-col v-for="i in 10" :key="i" cols="12" md="6">
          <v-card>
            <v-card-title>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    <template v-if="i % 3 === 0">
                      <v-chip label dark color="red">Live</v-chip>
                    </template>
                    <template v-else>
                      <v-chip label dark color="gray">Offline</v-chip>
                    </template>

                    Titel des Kurses / der Veranstaltung {{ i }}
                  </v-list-item-title>
                  <v-list-item-subtitle class="title">
                    <template v-if="i % 2 === 0">
                      Vorlesung
                    </template>
                    <template v-else>
                      Übung
                    </template>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle class="subtitle-1">
                    Dozent {{ i }}
                  </v-list-item-subtitle>
                  <v-list-item-subtitle class="subtitle-2">
                    Do. - 11:00 Uhr - 13:00 Uhr, Fr. - 09:00 Uhr - 12:00 Uhr
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card-title>
            <v-card-actions>
              <v-spacer />

              <v-btn color="primary" nuxt :to="`courses/${i}`">
                Zum Kurs&nbsp;
                <v-icon small>fa-chevron-circle-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
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

<script lang="ts"></script>
