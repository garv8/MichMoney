import React, { useState } from "react";
import ChoroplethMap from "./Choropleth";

const Forex = () => {

  const [labelContent, setLabelContent] = useState("");

  const updateLabelContent = (content) => {
    setLabelContent(content);
  };

  return (
    <div className="w-full flex">
      <div className="w-[75%] h-full">
        <ChoroplethMap onHover={updateLabelContent} />
      </div>
      <div className="w-[25%] min-h-full flex items-center justify-center mx-auto">
        <div className="max-w-[75%%] whitespace-normal text-center">
          <h2 className="text-2xl text-white font-bold">Selected Country:</h2>
          <p className="text-2xl text-white">{labelContent}</p>
        </div>
      </div>
    </div>
  );
};

export default Forex;
