function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    $("#chat-log").append(`<div class="user">You: ${userInput}</div>`);
    document.getElementById("user-input").value = "";
    $("#chat-log").append(`<div class="bot">Bhairav 🐶 is typing...</div>`);

    fetch("/chat", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(res => res.json())
    .then(data => {
        $(".bot:last").remove();  // remove typing message
        $("#chat-log").append(`<div class="bot">Bhairav 🐶: ${data.reply}</div>`);
        $("#chat-log").scrollTop($("#chat-log")[0].scrollHeight);
    });
}

