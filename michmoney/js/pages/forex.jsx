import React, { useState } from "react";
import ChoroplethMap from "./Choropleth";

const Forex = () => {
  const [tooltipContent, setTooltipContent] = useState("");

  return (
    <div className="flex">
      <div className="w-[75%] ">
        <ChoroplethMap tooltipContent={tooltipContent} setTooltipContent={setTooltipContent} />
      </div>
      <div class="w-[25%] h-full text-white">
        <h1>{tooltipContent}</h1>
      </div>
    </div>
  );
};

export default Forex;
