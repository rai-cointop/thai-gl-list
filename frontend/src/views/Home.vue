<template>
  <v-container>
    <v-row>
      <v-col v-for="person in individuals" :key="person.名前" cols="12" sm="6" md="4">
        <ActressCard :actress="person" @click="goToDetail(person.CP名)" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ActressCard from '@/components/ActressCard.vue'
import { useRouter } from 'vue-router'

const individuals = ref([])
const router = useRouter()

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

onMounted(async () => {
  const res = await fetch(`${apiBaseUrl}/api/individuals`)
  individuals.value = await res.json()
})

const goToDetail = (cpName) => {
  router.push(`/detail/${cpName}`)
}
</script>
