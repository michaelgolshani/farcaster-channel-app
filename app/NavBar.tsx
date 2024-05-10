import Link from "next/link";
import React from "react";

const NavBar = () => {
  return (
    <div className="flex p-5 justify-between">
      <Link href="/" className="flex">
        <div className="border-purple border-solid">&#x2191;</div>
        <div className="font-thin">higher</div>
        <div className="font-normal">Cast</div>
      </Link>
      <div className="flex space-x-4">
        <div>Trending Channels</div>
        <div>\</div>
        <div> Zora</div>
        <div>\</div>
        <div> 0xb25839439</div>
      </div>
      <div className="flex">Profile</div>
    </div>
  );
};

export default NavBar;
