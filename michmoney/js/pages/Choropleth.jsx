import React, { useEffect, useState } from "react";
import { csv } from "d3-fetch";
import { scaleLinear } from "d3-scale";
import * as d3 from "d3";
import {
  ComposableMap,
  Geographies,
  Geography,
  Sphere,
  Graticule
} from "react-simple-maps";

const geoUrl = "/static/util/worldgeo.json";

const colorScale = scaleLinear()
  .domain([-1, 1])
  .range(["#FF0000", "#00FF00"]);
const node = document.createElement('div');
// create a tooltip
const tooltip = d3.select(node)
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "2px")
    .style("border-radius", "5px")
    .style("padding", "5px")
    .style("margin-bottom", '51px')

const ChoroplethMap = ({ onHover }) => {
  const [data, setData] = useState([]);
  const [curr_year, setCurrYear] = useState(1995); // 1995 - 2017

  useEffect(() => {
    const fetchData = async () => {
      // csv('/static/util/vulnerability.csv').then((data) => {
      //   setData(data["1995"]);
      //   console.log(data["1995"]);
      // });

      const newData = await csv('/static/util/forex_prices.csv');
      setData(newData);};

    fetchData();

    const interval = setInterval(() => {
      setCurrYear((prevYear) => (prevYear < 2017 ? prevYear + 1 : 1995));
      fetchData();
    }, 5000);

    return () => clearInterval(interval);
  }, [curr_year]);

  const handleMouseEnter = (geo, currentData) => {
    const tooltipText = currentData
      ? `${geo.properties.name}: ${parseFloat(currentData[String(curr_year)]).toFixed(3)}`
      : `${geo.properties.name}: N/A`;
    onHover(tooltipText);
  };

  const handleMouseLeave = () => {
    onHover("");
  };

  return (
    <div>
      <ComposableMap
        projectionConfig={{
          rotate: [-10, 0, 0],
          scale: 135,
        }}
      >
        <Sphere stroke="#444444" strokeWidth={0.5} />
        <Graticule stroke="#444444" strokeWidth={0.5} />
        {data.length > 0 && (
          <Geographies geography={geoUrl}>
            {({ geographies }) =>
              geographies.map((geo) => {
                const d = data.find((s) => s.ISO3 === geo.id);
                //console.log(d);
                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={d ? colorScale(+d[String(curr_year)]) : "#000"}
                    style={{
                      default: {
                        fill: d ? colorScale(+d[String(curr_year)]) : "#000",
                        outline: "none",
                      },
                      hover: {
                        fill: d ? colorScale(+d[String(curr_year)]) : "#000",
                        outline: "none",
                        cursor: "crosshair",
                      },
                      pressed: {
                        fill: d ? colorScale(+d[String(curr_year)]) : "#000",
                        outline: "none",
                      },
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
    </div>
  );
};

export default ChoroplethMap;
