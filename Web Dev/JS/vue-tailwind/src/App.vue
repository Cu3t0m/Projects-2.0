<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import HelloWorld from './components/HelloWorld.vue'
import BodyContent from './BodyContent.vue'
</script>

<template>

  <HelloWorld msg="Welcome!" />

  <main>
    <!--  -->
    <BodyContent />
  </main>
</template>

<style>
#heading {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  align-items: center;
  color: #2c3e50;
  margin-top: 20%;
  /* margin-left: 10%;
  width: 50%; */
}

</style>
