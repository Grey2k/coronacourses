/* eslint-disable @typescript-eslint/explicit-function-return-type */

interface NotificationData {
  message: string
  type: string
  timeout: number
  icon: string
}

export type NotificationType = 'info' | 'success' | 'warning' | 'error'

export const state = () => ({
  show: false,
  message: '',
  type: '',
  icon: '',
  timerId: null,
})

export const mutations = {
  showNotification(state, data: NotificationData) {
    state.message = data.message
    state.type = data.type
    state.icon = data.icon

    state.show = true
  },
  removeNotification(state) {
    state.show = false
  },
  setTimeoutTimer(state, id) {
    state.timerId = id
  },
}

export const actions = {
  setNotification({ commit, state }, data: NotificationData) {
    commit('showNotification', data)

    const { timerId } = state
    if (timerId) {
      clearTimeout(timerId)
    }

    const id = setTimeout(
      () => {
        commit('removeNotification')
      },
      data.timeout ? data.timeout * 1000 : 3000
    )

    commit('setTimeoutTimer', id)
  },
  info({ dispatch }, data: NotificationData) {
    dispatch('setNotification', {
      ...data,
      type: 'info',
      icon: 'fa-info-circle',
    })
  },
  success({ dispatch }, data: NotificationData) {
    dispatch('setNotification', {
      ...data,
      type: 'success',
      icon: 'fa-check-circle',
    })
  },
  warning({ dispatch }, data: NotificationData) {
    dispatch('setNotification', {
      ...data,
      type: 'warning',
      icon: 'fa-exclamation-triangle',
    })
  },
  error({ dispatch }, data: NotificationData) {
    dispatch('setNotification', {
      ...data,
      type: 'error',
      icon: 'fa-exclamation-circle',
    })
  },
}
