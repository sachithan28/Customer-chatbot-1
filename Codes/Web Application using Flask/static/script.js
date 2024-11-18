document.getElementById("send-button").onclick = async function() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Display user's message
    addMessage(userInput, "user");
    document.getElementById("user-input").value = ""; // Clear input

    // Send the message to the Flask backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    const botMessage = data.response;
    addMessage(botMessage, "bot");
};

function addMessage(text, sender) {
    const messagesDiv = document.getElementById("messages");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${sender}`;
    messageElement.textContent = text;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to the bottom
}
