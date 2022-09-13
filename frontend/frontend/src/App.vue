<template>
<div id="app">
  <Nav/>
    <div class="container mt-5">
      <router-view/>
    </div>
</div>
</template>

<script>
import Nav from '@/components/Nav.vue'
export default {
  name: "App",
  components: {
      Nav
    }
}
</script>
<style>
  @keyframes fadein {
    from {opacity: 0;}
    to {opacity: 100;}
  }
  #app{
    animation-name: fadein;
    animation-duration: 2s;
  }
</style>
