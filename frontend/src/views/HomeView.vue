<script setup>
import { useArticleStore } from '../stores/articles'
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const store = useArticleStore()

onMounted(() => {
  store.fetchArticles()
})
</script>

<template>
  <main>
    <h1>Articles List</h1>
    <div v-if="store.loading">Loading...</div>
    <div v-else>
      <div v-for="article in store.articles" :key="article.id">
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <RouterLink :to="'/articles/' + article.id">Read more</RouterLink>
        <hr>
      </div>
    </div>
  </main>
</template>