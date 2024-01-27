import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { IndexForex, IndexEarnings } from "./index";

// Create a root
const root_forex = createRoot(document.getElementById("reactEntryForex"));

const root_earnings = createRoot(document.getElementById("reactEntryEarnings"));

// This method is only called once
// Insert the post component into the DOM
root_forex.render(
  <StrictMode>
    <IndexForex />
  </StrictMode>,
);

root_earnings.render(
  <StrictMode>
    <IndexEarnings />
  </StrictMode>,
);
