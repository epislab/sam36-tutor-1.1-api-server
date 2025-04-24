"use client";
export const dynamic = "force-dynamic"
// 클라이언트 컴포넌트로 선언
import SignupForm from "@/domain/(account)/auth/user/components/signup/SignupForm";



export default function Signup() {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-96">
        <h2 className="text-2xl font-bold text-center mb-4">Sign Up</h2>
        <SignupForm />
        <p className="text-center text-sm text-gray-600 mt-4">
          Already have an account? <a href="/auth/login" className="text-blue-500">Log in</a>
        </p>
      </div>
    </div>
  );
}
