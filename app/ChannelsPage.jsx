import React from "react";
import ChannelTable from "./ChannelTable";

const ChannelsPage = async () => {
  return (
    <>
      <div className="channel-page flex space-x-4 pt-10">
        <div className="flex-col w-4/6">
          <div className="font-fredokan text-3xl pb-10">Trending Channels</div>
          <ChannelTable />
        </div>
        <div className="font-fredokan text-3xl w-2/6 border-solid border-white">
          Top Channels
        </div>
      </div>
    </>
  );
};

export default ChannelsPage;
