<template lang="pug">
#app
  Header
  Aside
  Main
  Footer
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import Header from "./components/globals/Header.vue"
import Aside from "./components/globals/Aside.vue"
import Main from "./components/globals/Main.vue"
import Footer from "./components/globals/Footer.vue"

@Component({
  components: {
    Header,
    Aside,
    Main,
    Footer
  }
})
export default class App extends Vue {}
</script>

<style lang="stylus" scoped></style>
