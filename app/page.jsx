"use client";

import Image from "next/image";
import Link from "next/link";
import { useState, useEffect } from "react";
import ChannelsPage from "./ChannelsPage";
import NavBar from "./NavBar";

export default function Home() {
  return (
    <>
      <NavBar />
      <ChannelsPage />
    </>
  );
}
