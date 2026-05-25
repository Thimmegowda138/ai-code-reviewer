import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [code, setCode] = useState("");
  const [review, setReview] = useState("");

  const handleReview = async () => {

    try {

      const response = await axios.post(
        "https://ai-code-reviewer-backend-idxj.onrender.com/review",
        {
          code: code,
        }
      );

      console.log("FULL RESPONSE:", response);

      setReview(response.data.review);

    } catch (error) {

      console.log("ERROR:", error);

      setReview("Backend connection failed");
    }
  };

  return (
    <div className="App">

      <h1>AI Code Reviewer</h1>

      <textarea
        rows="10"
        cols="50"
        placeholder="Paste your code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <br /><br />

      <button onClick={handleReview}>
        Analyze Code
      </button>

      <h2>Review Result:</h2>

      <div
        style={{
          border: "1px solid gray",
          padding: "10px",
          marginTop: "10px",
          whiteSpace: "pre-wrap",
        }}
      >
        {review}
      </div>

    </div>
  );
}

export default App;