"use client";

import Image from "next/image";
import Link from "next/link";
import { useState, useEffect } from "react";

export default function Home() {
  // Pull data from an api so that we can show it on the front page of the app

  const [data, setData] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/api/python");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setData(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  console.log("data", data);

  if (!data) return <div>Loading...</div>;

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold text-center">
        Welcome to your Next.js app
      </h1>
      <p className="text-center">
        This is a simple Next.js app that uses a Python API to fetch data.
      </p>
      <div className="flex flex-col items-center">
        <Image
          src="/python-logo.png"
          alt="Python logo"
          width={200}
          height={200}
        />
        <h2 className="text-2xl font-bold">Python data</h2>
        {/* <ul className="flex flex-col items-center">
          {data && data.map((item) => (
            <li key={item.id} className="text-lg">
              {item.name}
            </li>
          ))}
        </ul> */}
      </div>
      <div className="flex flex-col items-center">
        <Link href="/about">About Us</Link>
        <Link href="/contact">Contact Us</Link>
      </div>
    </main>
  );
}
