<template lang="pug">
section#home-hero.hero.is-fullheight-with-navbar
  div.hero-body
    div.container.has-text-centered
      p.title AIがあなたの牌譜をレビューします！
      b-field
        b-input(
          v-model="mjlogWatchUrl"
          placeholder="http://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
          type="url"
          icon="link"
          expanded
        )
        p.control
          button.button.is-primary(
            @click="reserveReview"
          ) レビュー
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import axios from "axios"

@Component
export default class HomeHero extends Vue {
  mjlogWatchUrl = ""

  async reserveReview() {
    await axios.post("/api/review/create", {
      // eslint-disable-next-line @typescript-eslint/camelcase
      mjlog_watch_url: this.mjlogWatchUrl
    })
  }
}
</script>

<style lang="stylus" scoped></style>
