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
    <img v-if="article.image" :src="article.image" style="max-width: 100%; height: auto; border-radius: 10px; margin-bottom: 20px;">

    <h1>{{ article.title }}</h1>

    <p>{{ article.text }}</p>

    <hr>
    
    <h3>Коментарі:</h3>
    <div v-if="article.comments && article.comments.length">
      <div v-for="comment in article.comments" :key="comment.id" style="background: #f9f9f9; padding: 10px; margin-bottom: 10px; border-radius: 5px;">
        <strong>{{ comment.author_name || 'Гість' }}</strong>:
        <span style="display: block; margin-top: 5px;">{{ comment.text }}</span>
      </div>
    </div>
    <div v-else>
      <p style="color: gray;">Коментарів поки немає.</p>
    </div>

    <br>
    <RouterLink to="/">← Назад до списку</RouterLink>
  </div>
  <div v-else>
    Loading...
  </div>
</template>
<style scoped>
h1 { margin-bottom: 20px; color: #2c3e50; }
p { line-height: 1.6; font-size: 1.1rem; }
</style>