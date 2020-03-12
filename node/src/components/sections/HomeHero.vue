<template lang="pug">
section#home-hero.hero.is-fullheight-with-navbar
  div.hero-body
    div.container.has-text-centered
      p.title AIがあなたの牌譜をレビューします！
      form.form 
        b-field
          b-input(
            placeholder="http://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
            type="url"
            icon="link"
          )
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"

@Component
export default class HomeHero extends Vue {}
</script>

<style lang="stylus" scoped></style>
