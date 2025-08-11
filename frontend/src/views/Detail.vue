<template>
  <v-container v-if="data">
    <!-- ホームに戻るボタン（上部） -->
    <v-btn color="primary" class="mb-4" @click="$router.push('/')">ホームに戻る</v-btn>

    <v-img :src="`/images/${data.cp.画像}`" height="300px" contain />
    <h2>{{ data.cp.ペア名 }}</h2>
    <p>事務所: {{ data.cp.事務所 }}</p>
    <p>出演作品: {{ cpWorks }}</p>
    <p>曲: {{ cpSongs }}</p>

    <v-divider class="my-4" />
    
    <div v-for="person in data.individuals" :key="person.名前">
      <v-img :src="`/images/${person.画像}`" height="150px" contain />
      <p><strong>{{ person.名前 }}</strong></p>
      <p>誕生日: {{ person.誕生日 }}</p>
      <p>身長: {{ person.身長 }}</p>
      <p>絵文字: {{ person.絵文字 }}</p>
      <v-divider class="my-4" />
    </div>

  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const data = ref(null)

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

const cpWorks = ref('')
const cpSongs = ref('')

onMounted(async () => {
  const res = await fetch(`${apiBaseUrl}/api/details/${route.params.cpName}`)
  data.value = await res.json()

  if (data.value.cp) {
    cpWorks.value = data.value.cp.出演作品 ? data.value.cp.出演作品.split('|').join(', ') : ''
    cpSongs.value = data.value.cp.曲 ? data.value.cp.曲.split('|').join(', ') : ''
  }
})
</script>
