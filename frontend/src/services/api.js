const API_URL = "https://8r4fbm7t-8000.inc1.devtunnels.ms/ask";

export const sendQuery = async (question) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    throw new Error("API error");
  }

  return response.json();
};
