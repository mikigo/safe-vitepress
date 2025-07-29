<template>
  <div>
    <button 
      v-if="!isAuthenticated && !loading" 
      class="login-btn" 
      @click="showLoginModal = true"
      title="Log in to access protected content"
    >
      <span class="login-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
      </span>
    </button>

    <!-- Login Modal -->
    <teleport to="body" v-if="showLoginModal">
        <div class="modal-overlay" @click="showLoginModal = false">
          <div class="modal-container" @click.stop>
            <div class="modal-header">
                <h2>Login</h2>
                <button class="close-btn" @click="showLoginModal = false">×</button>
              </div>
              <div class="modal-body">
          <div v-if="error" class="error-message">{{ error }}</div>
          <form @submit.prevent="handleSubmit">
            <div class="form-group">
              <label for="username">Username</label>
              <input
                id="username"
                v-model="username"
                type="text"
                required
                placeholder="Enter your username"
              />
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input
                id="password"
                v-model="password"
                type="password"
                required
                placeholder="Enter your password"
              />
            </div>
            <button
              type="submit"
              class="submit-btn"
              :disabled="loading"
            >
              <span v-if="loading">Logging in...</span>
              <span v-else>Login</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </teleport>
</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuth } from '../auth/authService';

const { isAuthenticated, loading, login } = useAuth();
const showLoginModal = ref(false);
const username = ref('');
const password = ref('');
const error = ref('');

const handleSubmit = async () => {
  error.value = '';
  const success = await login(username.value, password.value);
  if (success) {
    showLoginModal.value = false;
    username.value = '';
    password.value = '';
  } else {
    error.value = 'Invalid username or password';
  }
};
</script>

<style>
.login-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0.6rem 1rem;
  font-size: 0.9rem;
  font-weight: 500;
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-right: 0.75rem;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.modal-container {
  background-color: var(--vp-c-bg);
  border-radius: 8px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--vp-c-divider);
}

.modal-header h2 {
  margin: 0;
  font-size: 1.25rem;
  color: var(--vp-c-text-1);
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--vp-c-text-2);
}

.modal-body {
  padding: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 1rem;
}

.form-group input:focus {
  outline: none;
  border-color: var(--vp-c-brand);
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--vp-c-brand);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover:not(:disabled) {
  background-color: var(--vp-c-brand-dark);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.error-message {
  background-color: rgba(248, 215, 218, 0.1);
  color: var(--vp-c-danger);
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  text-align: center;
}

.login-btn:hover {
  background-color: var(--vp-c-brand-dark);
  transform: translateY(-1px);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
}

.login-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.dark .login-btn {
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.dark .login-btn:hover {
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4);
}

@media (max-width: 768px) {
  .login-btn {
    padding: 0.5rem 0.75rem;
  }
}
</style>