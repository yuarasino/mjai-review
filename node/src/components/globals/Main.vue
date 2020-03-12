<template lang="pug">
main#main
  router-view
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"

@Component
export default class Main extends Vue {}
</script>

<style lang="stylus" scoped></style>
