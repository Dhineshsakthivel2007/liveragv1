import React, { useState } from "react";
import { sendQuery } from "../services/api";

const ChatBox = () => {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input) return;

    setLoading(true);
    setResponse("");

    try {
      const data = await sendQuery(input);
      setResponse(data.answer || "No response from backend");
    } catch (error) {
      setResponse("❌ Backend not reachable");
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <textarea
        placeholder="Ask something..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={handleSend}>Send</button>

      {loading && <p>⏳ Processing...</p>}

      {response && (
        <div className="response-box">
          <strong>Response:</strong>
          <p style={{ whiteSpace: "pre-line" }}>
  {response}
</p>
        </div>
      )}
    </div>
  );
};

export default ChatBox;
