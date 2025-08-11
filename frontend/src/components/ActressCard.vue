<template>
  <v-card class="ma-2" @click="$emit('click')" hover>
    <v-img :src="`/images/${actress.画像}`" height="200px" contain />
    <v-card-title>{{ actress.名前 }}</v-card-title>
  </v-card>
</template>

<script setup>
const props = defineProps(['actress'])
</script>
