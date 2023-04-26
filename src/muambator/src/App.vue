<template>
  <div id="app">
    <Homepage></Homepage>
  </div>
</template>

<script>
import Homepage from "./components/Homepage.vue";

export default {
  name: 'App',
  components: {
    Homepage,
  }
}
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 6rem;
}

</style>
