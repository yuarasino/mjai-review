<template lang="pug">
#home
  HomeHero
  HomeReview
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import HomeHero from "../components/sections/HomeHero.vue"
import HomeReview from "../components/sections/HomeReview.vue"

@Component({
  components: {
    HomeHero,
    HomeReview
  }
})
export default class Home extends Vue {}
</script>
