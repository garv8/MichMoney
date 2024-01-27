import React, { useEffect, useState } from "react";
import Forex from "./components/forex.jsx";
import Earnings from "./components/earnings.jsx";

function IndexForex() {
    return (
        <div className="bg-gray-dark">
            <div id="content" className="mx-16" style={{width:"-webkit-fill-available"}}>
                <div>
                    <Forex name={name} className="flex"/>
                </div>
            </div>
        </div>
    )
}

function IndexEarnings() {
    return (
        <div className="bg-gray-dark">
            <div id="content" className="mx-16" style={{width:"-webkit-fill-available"}}>
                <div>
                    <Earnings name={name} className="flex"/>
                </div>
            </div>
        </div>
    )
}

export { IndexForex, IndexEarnings };
