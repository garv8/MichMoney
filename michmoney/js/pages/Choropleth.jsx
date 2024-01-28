import React, { useEffect, useState } from "react";
import { csv } from "d3-fetch";
import { scaleLinear } from "d3-scale";
import {
  ComposableMap,
  Geographies,
  Geography,
  Sphere,
  Graticule
} from "react-simple-maps";
import { Tooltip } from "react-tooltip";

const geoUrl = "/static/util/worldgeo.json";

const colorScale = scaleLinear()
  .domain([0.29, 0.68])
  .range(["#FF0000", "#00FF00"]);

const ChoroplethMap = () => {
  const [data, setData] = useState([]);
  const [tooltipContent, setTooltipContent] = useState("");

  useEffect(() => {
    csv('/static/util/vulnerability.csv').then((data) => {
      setData(data);
    });
  }, []);

  const handleMouseEnter = (geo, currentData) => {
    const tooltipText = currentData ? `${geo.properties.name}: ${currentData["2017"]}` : `${geo.properties.name}: N/A`;
    setTooltipContent(tooltipText);
  };

  const handleMouseLeave = () => {
    setTooltipContent("");
  };

  return (
    <div>
      <ComposableMap
        projectionConfig={{
          rotate: [-10, 0, 0],
          scale: 147
        }}
      >
        <Sphere stroke="#444444" strokeWidth={0.5} />
        <Graticule stroke="#444444" strokeWidth={0.5} />
        {data.length > 0 && (
          <Geographies geography={geoUrl}>
            {({ geographies }) =>
              geographies.map((geo) => {
                const d = data.find((s) => s.ISO3 === geo.id);
                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={d ? colorScale(+d["2017"]) : "#000"}
                    style={{
                      default: {
                        fill: d ? colorScale(+d["2017"]) : "#000",
                        outline: "none"
                      },
                      hover: {
                        fill: d ? colorScale(+d["2017"]) : "#000",
                        outline: "none",
                        cursor: "pointer"
                      },
                      pressed: {
                        fill: d ? colorScale(+d["2017"]) : "#000",
                        outline: "none"
                      }
                    }}
                    onMouseEnter={() => handleMouseEnter(geo, d)}
                    onMouseLeave={handleMouseLeave}
                  />
                );
              })
            }
          </Geographies>
        )}
      </ComposableMap>
      <div style={{ position: 'relative' }}>
        <Tooltip style={{ visibility: 'visible', position: 'absolute', top: '0', left: '0' }} className="h-full w-full bg-white">{tooltipContent}</Tooltip>
      </div>
    </div>
  );
};

export default ChoroplethMap;
