let apiKey = "";

async function initializeAgent() {
  const input = document.getElementById("apiKey");
  const key = input.value.trim();
  const status = document.getElementById("status");

  if (!key) {
    status.textContent = "Please enter an API key.";
    return;
  }

  status.textContent = "Validating API key...";

  try {
    const response = await fetch("/api/validate-key", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        api_key: key,
      }),
    });

    const data = await response.json();

    if (!data.valid) {
      status.textContent = "❌ Invalid or unusable API key.";
      return;
    }

    apiKey = key;

    input.value = "";
    input.disabled = true;

    document.getElementById("message").disabled = false;
    document.getElementById("message").placeholder =
      "Ask a mathematical question...";

    document.getElementById("sendButton").disabled = false;

    status.textContent = "✓ Agent initialized. Ready for testing.";
  } catch (error) {
    status.textContent = "❌ Could not connect to the server.";
  }
}

async function sendMessage() {
  const messageInput = document.getElementById("message");
  const message = messageInput.value.trim();

  if (!apiKey) {
    alert("Initialize the agent first.");
    return;
  }

  if (!message) {
    return;
  }

  addMessage("You", message);
  messageInput.value = "";

  const response = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: message,
      api_key: apiKey,
    }),
  });

  const data = await response.json();

  addMessage("Agent", data.answer || data.error || "Something went wrong.");
}

function addMessage(sender, message) {
  const chat = document.getElementById("chat");

  const div = document.createElement("div");

  div.className = `message ${sender.toLowerCase()}`;

  div.innerHTML = `
        <div class="message-label">${sender}</div>
        <div class="message-bubble">${message}</div>
    `;

  chat.appendChild(div);

  if (window.MathJax) {
    MathJax.typesetPromise([div]);
  }

  chat.scrollTop = chat.scrollHeight;
}
