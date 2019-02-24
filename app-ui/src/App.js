import React, { useEffect, useState } from "react";
import "./App.css";

const fetchCounts = () =>
  fetch(`${process.env.REACT_APP_API_URL}/counts`).then(response =>
    response.json()
  );

const updateCounts = counts =>
  fetch(`${process.env.REACT_APP_API_URL}/counts`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ counts })
  }).then(response => response.json());

const App = () => {
  const [counts, setCounts] = useState(0);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    fetchCounts().then(({ counts }) => {
      setCounts(counts);
      setLoading(false);
    });
  }, []);

  const updateRemoteCounts = async counts => {
    const loadingTimeout = setTimeout(() => {
      setLoading(true);
    }, 150);

    await updateCounts(counts);
    clearTimeout(loadingTimeout);

    setLoading(false);
    setCounts(counts);
  };

  return (
    <div className="app">
      <button
        disabled={isLoading}
        onClick={() => updateRemoteCounts(counts + 1)}
        className="operation-btn"
      >
        +
      </button>
      {isLoading ? "⌛" : counts}
      <button
        disabled={isLoading}
        onClick={() => updateRemoteCounts(counts - 1)}
        className="operation-btn"
      >
        -
      </button>
    </div>
  );
};

export default App;
