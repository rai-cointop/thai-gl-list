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

onMounted(async () => {
  // 2つのJSONを並行して取得
  const [cpRes, indRes] = await Promise.all([
    fetch('/data/cp_data.josn'),
    fetch('/data/individual_data.json')
  ])

  const cpList = await cpRes.json()
  const individualsList = await indRes.json()

  const cpName = route.params.cpName

  // 指定されたCP名に該当するCPデータと個人情報を取得
  const cp = cpList.find(item => item.CP名 === cpName)
  const members = individualsList.filter(item => item.CP名 === cpName)

  data.value = {
    cp,
    individuals: members
  }
})
</script>
