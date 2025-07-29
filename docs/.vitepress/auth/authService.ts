import { ref, computed, readonly } from 'vue';
import axios from 'axios';

// 后端API地址
const API_URL = import.meta.env.API_URL || 'http://localhost:8000';

// 状态管理
const token = ref<string | null>(localStorage.getItem('token'));
const user = ref<any>(null);
const loading = ref(false);
const error = ref<string | null>(null);

// 创建axios实例
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器添加token
api.interceptors.request.use(
  (config) => {
    if (token.value) {
      config.headers.Authorization = `Bearer ${token.value}`;
    }
    return config;
  },
  (err) => Promise.reject(err)
);

// 初始化认证状态
export async function initAuth() {
  if (!token.value) return;

  loading.value = true;
  try {
    const response = await api.get('/users/me');
    user.value = response.data;
  } catch (err) {
    console.error('Failed to fetch user data:', err);
    logout(); // 令牌无效时登出
  } finally {
    loading.value = false;
  }
}

// 登录功能
export async function login(username: string, password: string) {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.post('/token', new URLSearchParams({
      username,
      password,
      grant_type: 'password'
    }), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    const { access_token } = response.data;
    token.value = access_token;
    localStorage.setItem('token', access_token);

    // 获取用户信息
    await initAuth();
    return true;
  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Login failed';
    return false;
  } finally {
    loading.value = false;
  }
}

// 登出功能
export async function logout() {
  token.value = null;
  user.value = null;
  localStorage.removeItem('token');
}

// 认证状态导出
export const useAuth = () => ({
  isAuthenticated: computed(() => !!token.value && !!user.value),
  user: readonly(user),
  loading: readonly(loading),
  error: readonly(error),
  login,
  logout,
  initAuth
});