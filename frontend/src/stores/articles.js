import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('articleStore', {
  state: () => ({
    articles: [],
    loading: false
  }),
  actions: {
    async fetchArticles() {
      this.loading = true
      try {
        const response = await axios.get('http://localhost:8000/api/articles/')
        this.articles = response.data
      } catch (error) {
        console.error(error)
      } finally {
        this.loading = false
      }
    },
    async fetchArticleById(id) {
      try {
        const response = await axios.get(`http://localhost:8000/api/articles/${id}/`)
        return response.data
      } catch (error) {
        console.error(error)
      }
    }
  }
})