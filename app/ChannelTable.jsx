"use client";

import React, { useEffect, useState } from "react";
import "./ChannelTable.css";

const ChannelTable = () => {
  const [channels, setChannels] = useState([]);
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const response = await fetch("/api/farcaster/trending_channels");
        const response = await fetch('/api/channels/trending')
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        console.log("data", data)
        setData(data);
        setChannels(data.channels);
        // setChannels(data)
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  console.log("data", data);
  console.log("channels", channels);

  if (channels.length == 0) {
    return <div>Loading..</div>;
  }

  return (
    <div>
      <ul
        className="flex-col font-sans overflow-y-auto max-h-96 scroll"
        style={{ maxHeight: 35 + "em" }}
      >
        {channels.map((channel) => (
          <li
            className="py-6  bg-purple-950 rounded-lg"
            key={channel.cast_count_1d}
          >
            <div className="pl-4 text-2xl">{channel.channel.name}</div>
          </li> // Assuming each channel has a unique ID and name
        ))}
      </ul>
    </div>
  );
};

export default ChannelTable;
