import { useState } from "react";
import axios from "axios";

function App() {

  const [code, setCode] = useState("");
  const [review, setReview] = useState("");

  const handleReview = async () => {

    try {

      const response = await axios.post(
        "http://localhost:8000/review",
        {
          code: code,
        }
      );

      console.log(response.data);

      setReview(response.data.review);

    } catch (error) {

      console.log(error);

      setReview("Error connecting to backend");

    }
  };

  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "Arial",
      }}
    >

      <h1>AI Code Reviewer</h1>

      <textarea
        rows="12"
        cols="70"
        placeholder="Paste your code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <br />
      <br />

      <button onClick={handleReview}>
        Analyze Code
      </button>

      <h2>Review Result:</h2>

      <pre>{review}</pre>

    </div>
  );
}

export default App;