import axios from 'axios'
import { getAccessToken } from './authToken'

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  withCredentials: true  // 👉 쿠키 자동 전송
  // Axios 사용 시 반드시 withCredentials: true 옵션이 필요합니다.
})

api.interceptors.request.use((config) => {
  const accessToken = getAccessToken()
  if (accessToken) {
    console.log('🆔🆔🆔🆔🆔token', accessToken)
    config.headers.Authorization = `Bearer ${accessToken}`
  }
  return config
})

export default api
