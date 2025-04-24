"use client";

import { useState, useEffect, FormEvent, ChangeEvent } from 'react'
import { signIn, useSession, signOut } from 'next-auth/react'
import { useRouter } from 'next/navigation'
import axios from 'axios'

export default function Login() {
  const [email, setEmail] = useState('')
  const { data: session, status } = useSession()
  const router = useRouter()
  const [isLogged, setIsLogged] = useState(false)

  // 세션 상태 변경 감지
  useEffect(() => {
    if (session && !isLogged) {
      setIsLogged(true)
      console.log('🔵 Session Status:', status)
      console.log('🔵 Session Data:', session)
      console.log('👧🏻👧🏻👧🏻👧🏻Access Token:', session.accessToken)
      console.log('🦣🦣🦣🦣Refresh Token:', session.refreshToken)
      console.log('⏰ Expires At:', session.expiresAt)

      // 시나리오 1: gateway에 토큰 전달
      const sendTokensToGateway = async () => {
        try {
          const response = await axios.post('http://localhost:8000/api/auth/tokens', {
            accessToken: session.accessToken,
            refreshToken: session.refreshToken,
            expiresAt: session.expiresAt
          })

          if (response.data.status === 'SUCCESS') {
            // 시나리오 2: gateway에서 SUCCESS 응답을 받으면 로컬 JWT 삭제
            await signOut({ redirect: false })
            router.push('/')
          } else {
            console.error('❌ Token transfer failed:', response.data.message)
          }
        } catch (error) {
          console.error('❌ Error sending tokens to gateway:', error)
        }
      }

      if (session.accessToken) {
        sendTokensToGateway()
      }
    }
  }, [session, status, router, isLogged])

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    alert(`입력한 이메일: ${email}`)
  }

  const handleEmailChange = (e: ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value)
  }

  const handleGoogleLogin = async () => {
    try {
      const result = await signIn('google', { 
        callbackUrl: '/',
        redirect: false
      })
      console.log('🎯 Login Result:', result)
    } catch (error) {
      console.error('❌ Login failed:', error)
    }
  }

  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-white px-4">
      <div className="max-w-md w-full space-y-6 text-center">
        <h1 className="text-3xl font-extrabold text-gray-900">
          먼저 이메일부터 입력해 보세요
        </h1>
        <p className="text-sm text-gray-600">
          직장에서 사용하는 <span className="font-semibold">이메일 주소</span>로 로그인하는 걸 추천드려요.
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="email"
            required
            placeholder="name@work-email.com"
            value={email}
            onChange={handleEmailChange}
            className="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-600"
          />
          <button
            type="submit"
            className="w-full bg-purple-700 hover:bg-purple-800 text-white font-semibold py-3 rounded-md"
          >
            계속
          </button>
        </form>

        <div className="relative my-4">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-gray-300"></div>
          </div>
          <div className="relative flex justify-center text-sm">
            <span className="bg-white px-2 text-gray-500">또는</span>
          </div>
        </div>

        <div className="space-y-3">
          <button 
            onClick={handleGoogleLogin}
            className="w-full flex items-center justify-center border border-gray-300 rounded-md py-3 hover:bg-gray-50"
          >
            <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google logo" className="w-5 h-5 mr-2" />
            <span>Google 계정으로 로그인</span>
          </button>
          <button className="w-full flex items-center justify-center border border-gray-300 rounded-md py-3 hover:bg-gray-50">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/Naver_Logotype.svg" alt="Naver logo" className="w-5 h-5 mr-2" />
            <span>Naver 계정으로 로그인</span>
          </button>
        </div>

        <div className="text-sm text-gray-600 mt-6">
          이미 demo를 사용하고 있나요?{' '}
          <a href="#" className="text-blue-600 hover:underline">
            기존 워크스페이스에 로그인
          </a>
        </div>
      </div>
    </div>
  )
}
