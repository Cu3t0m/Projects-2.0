<script setup lang="ts">
import { ref } from 'vue'

const count = ref(0)
</script>

<template>

    <div class="button-thing">
      <button type="button" @click="count--" class="text-3xl bold">-</button>
      <p class="text-3xl bold">Count is {{ count }}</p>
      <button type="button" @click="count++" class="text-3xl bold">+</button>
    </div>
</template>

<style>
.button-thing {
  display: flex;
  flex-direction: row;
  position: inherit;
}

button {

  padding: 5px;
  background-color: #42b983;
  height: 50px;
  width: 50px;

}

p {
  background-color: #42b983;
  margin: 0px;
  padding: 5px;
  /* width: 180px; */
  height: 50px;
}
</style>