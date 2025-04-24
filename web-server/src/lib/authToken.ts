const ACCESS_TOKEN_KEY = 'access_token'

export const setAccessToken = (token: string) => {
  console.log('🆔🆔🆔🆔🆔setAccessToken :', token)
  localStorage.setItem(ACCESS_TOKEN_KEY, token)
}

export const getAccessToken = () => {
  if (typeof window !== 'undefined') {
    return localStorage.getItem(ACCESS_TOKEN_KEY)
  }
  return null
}

export const removeAccessToken = () => {
  localStorage.removeItem(ACCESS_TOKEN_KEY)
}
