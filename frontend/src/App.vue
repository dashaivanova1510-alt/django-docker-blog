<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<template>
  <div class="app-container">
    <header>
      <nav>
        <RouterLink to="/">Головна</RouterLink>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
}

header {
  border-bottom: 1px solid #ddd;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
}

nav a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 1.2rem;
  font-weight: bold;
}

nav a:hover {
  color: #42b883;
}
</style>