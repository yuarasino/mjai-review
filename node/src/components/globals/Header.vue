<template lang="pug">
header#header
  b-navbar
    template(slot="brand")
      b-navbar-item(tag="router-link" :to="{ path: '/' }") mjai-review
    template(slot="start")
      b-navbar-item(href="#") Home
      b-navbar-item(href="#") About
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"

@Component
export default class Header extends Vue {}
</script>

<style lang="stylus" scoped></style>
