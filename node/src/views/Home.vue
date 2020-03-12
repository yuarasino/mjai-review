<template lang="pug">
#home
  HomeHero
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import HomeHero from "../components/sections/HomeHero.vue"

@Component({
  components: {
    HomeHero
  }
})
export default class Home extends Vue {}
</script>
