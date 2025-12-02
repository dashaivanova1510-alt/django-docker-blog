<script setup>
import { useArticleStore } from '../stores/articles'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useArticleStore()
const article = ref(null)

onMounted(async () => {
  article.value = await store.fetchArticleById(route.params.id)
})
</script>

<template>
  <div v-if="article">
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
    <RouterLink to="/">Back to list</RouterLink>
  </div>
  <div v-else>
    Loading...
  </div>
</template>