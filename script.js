document.addEventListener('DOMContentLoaded', function () {
    const chatHistory = document.getElementById('chat-history');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function () {
        const userMessage = userInput.value;
        chatHistory.innerHTML += `<div class="user-message">${userMessage}</div>`;
        userInput.value = '';

        fetch('/get_response', {
            method: 'POST',
            body: new URLSearchParams({
                user_input: userMessage,
                chat_history: chatHistory.innerHTML
            })
        })
        .then(response => response.json())
        .then(data => {
            const assistantMessage = data.response;
            chatHistory.innerHTML += `<div class="assistant-message">${assistantMessage}</div>`;
            chatHistory.scrollTop = chatHistory.scrollHeight;
        });
    });
});
