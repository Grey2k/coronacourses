<!--
  - Copyright (c) 2019-2020 Pascal Sthamer, Konstantin Zisiadis und Jan Ziegler GbR.
  - All rights reserved.
  -->

<template>
  <v-snackbar
    v-if="show"
    :value="true"
    :timeout="0"
    :color="type"
    multi-line
    bottom
    right
  >
    <v-icon size="lg" class="mr-4">{{ icon }}</v-icon>
    <b>{{ message }}</b>

    <v-btn text @click="removeNotification">Okay</v-btn>
  </v-snackbar>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { NotificationType } from '../store/notification'

const notification = namespace('notification')

@Component
export default class Notification extends Vue {
  @notification.State('show')
  public show!: boolean

  @notification.State('message')
  public message!: string

  @notification.State('type')
  public type!: NotificationType | null

  @notification.State('icon')
  public icon!: string

  @notification.Mutation('removeNotification')
  public removeNotification!: () => void
}
</script>
