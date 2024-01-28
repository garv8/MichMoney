import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Forex from "./pages/forex";
import Earnings from "./pages/earnings";

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/earnings-analyzer/" element={<Earnings />} />
                <Route path="/forex/" element={<Forex />} />
            </Routes>
        </Router>
    );
};

export default App;