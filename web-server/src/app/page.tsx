"use client";

import Link from "next/link";
import { useState } from "react";

export default function CompanySearchPage() {
  const [query, setQuery] = useState("");
  const [companyName, setCompanyName] = useState("");

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    setCompanyName(query); // 검색어를 반영하여 회사명 업데이트
  };

  return (
    <div className="w-full">
      <div className="bg-gray-200 p-4 rounded shadow flex justify-between items-center">
  <h2 className="text-lg font-bold">Company Search</h2>

  <div>
    <Link href="/user/login" className="text-blue-500 no-underline hover:underline mr-4">로그인</Link><br/>
    <Link href="/user/signup" className="text-blue-500 no-underline hover:underline">회원가입</Link><br/>
    <Link href="/customer/list" className="text-blue-500 no-underline hover:underline">테스트</Link>
  </div>
</div>


      <main className=" mt-6 flex flex-col items-center">
        <section className="scrollable-section w-full max-w-lg p-4">
          {/* 검색 폼 */}
          <form className="form__companyName flex items-center gap-2" onSubmit={handleSearch}>
            <input
              type="search"
              placeholder="Search..."
              name="query"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full border border-gray-300 px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              className="search__button bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
            >
              Search
            </button>
          </form>

          {/* 검색 결과 */}
          <div className="mt-12 text-center">
            <h2 className="h2__companyName text-xl font-semibold text-gray-700">
              {companyName ? `Results for: ${companyName}` : "No results yet"}
            </h2>
          </div>
          <div>
            <Link href="/company/search">
              <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
                Target Company
              </button>
            </Link>
          </div>
        </section>
      </main>
    </div>
  );
}