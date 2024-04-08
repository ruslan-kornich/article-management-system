"use client"; // This is a client component
import { useEffect, useState } from 'react';

function ArticleList() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch('http://127.0.0.1:8000/articles/');
      const data = await res.json();
      setArticles(data);
    }

    fetchData();
  }, []);

  return (
    <ul className="grid gap-6">
      {articles.map((article) => (
        <li key={article.id} className="rounded-lg shadow-md p-6 bg-white">
          <h2 className="text-2xl font-semibold mb-2 text-black">{article.title}</h2>
          <p className="text-base text-black" dangerouslySetInnerHTML={{ __html: article.summary }}></p>
          <a href={article.link} className="text-blue-500 hover:text-blue-700" target="_blank" rel="noopener noreferrer">
            Continue reading...
          </a>
        </li>
      ))}
    </ul>
  );
}

export default function Page() {
  useEffect(() => {
    // Client-side logic will be here
  }, []);

  return (
    <main className="container mx-auto p-6">
      <ArticleList />
    </main>
  );
}
