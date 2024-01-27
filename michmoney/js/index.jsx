import React, { useEffect, useState } from "react";
import Data from "./components/data";

function Index() {
    return (
        <div className="bg-gray-dark">
            <div id="content" className="mx-16" style={{width:"-webkit-fill-available"}}>
                <div>
                    <Data name={name} className="flex"/>
                </div>
            </div>
        </div>
    )
}

export default Index;
