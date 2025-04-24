import React from "react";

interface Customer {
  user_id: string;
  email: string;
  name: string;
  password: string;
}

export default async function UserPage () {

  const res = await fetch('http://localhost:8000/api/customer/list', {
    cache: 'no-store', 
  });

  if (!res.ok) {
    throw new Error(`Failed to fetch customers: ${res.status}`);
  }

  const data: { customer_list: Customer[] } = await res.json(); // ✅ 응답 타입 명시
  const customers = data.customer_list;;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      
      <h3 className="text-4xl font-bold text-blue-500 mb-6">사용자 목록</h3>

      <div className="w-full max-w-4xl">
        <table className="w-full border-collapse border-4 border-gray-800 border-double shadow-lg bg-white">
          <thead>
            <tr className="bg-gray-200">
              <th className="border border-gray-800 px-4 py-2 text-left">이름</th>
              <th className="border border-gray-800 px-4 py-2 text-left">이메일</th>
            </tr>
          </thead>
          <tbody>
            {customers.map((customer) => (
              <tr key={customer.user_id} className="hover:bg-gray-100">
                <td className="border border-gray-800 px-4 py-2">{customer.name}</td>
                <td className="border border-gray-800 px-4 py-2">{customer.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

