import { defineConfig } from 'vitepress'
import { loadEnv } from 'vite'

const env = loadEnv('', process.cwd(), '')

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/',
  title: "Vitepress FastAPI Auth",
  description: "Vitepress with FastAPI Authentication", 
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Protected', link: '/markdown-examples' },
      { text: 'Public', link: '/non-protected' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Protected Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' },
          { text: 'Non-Protected Examples', link: '/non-protected' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/mikigo' }
    ],

    // Explicitly disable Algolia search
    search: {
      provider: 'local'
    }
  },

  // Define environment variables to expose to the client
  vite: {
    define: {
      'import.meta.env.API_URL': JSON.stringify(env.API_URL || 'http://localhost:8000')
    },
    optimizeDeps: {
      include: ['vue', 'axios']
    },
    server: {
      fs: {
        allow: ['..']
      }
    },
      
  }
})
