import React from "react";
import ChoroplethMap from "./Choropleth";

const Forex = () => {
      const forexData = {
        'USA': 75.5,
        'CAN': 60.8,
        'GBR': 82.3,
        // Add more countries and values as needed
      };
    
      return (
        <ChoroplethMap />
      );
    
};

export default Forex;