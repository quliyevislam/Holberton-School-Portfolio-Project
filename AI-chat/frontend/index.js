
const chatBox = document.querySelector('.chat-box');
const sendButton = document.querySelector('.send-button');
const inputField = document.querySelector('.input-field');


sendButton.addEventListener('click', (event) => {
    const userInput = inputField.value.trim();

    if (!userInput) {
        return;
    }

    const jsonData = {
        "message": userInput
    };

    inputField.value = '';

    const userMessage = document.createElement('div');
    const pUser = document.createElement('p');

    userMessage.classList.add('chat-message');
    userMessage.classList.add('user-message');
    userMessage.appendChild(pUser);

    pUser.textContent = userInput;
    chatBox.appendChild(userMessage);

    const loadingIndicator = document.createElement('div');
    loadingIndicator.classList.add('loading-indicator');
    chatBox.appendChild(loadingIndicator);

    fetch('http://0.0.0.0:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (result) {
            chatBox.removeChild(loadingIndicator);

            const aiMessage = document.createElement('div');
            const pAi = document.createElement('p');

            aiMessage.classList.add('chat-message');
            aiMessage.classList.add('ai-message');
            aiMessage.appendChild(pAi);

            result = result.replaceAll('**', '<br>');
            result = result.replaceAll('*', '');

            pAi.innerHTML = result
            chatBox.appendChild(aiMessage);

            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(function (error) {
            console.error('Error:', error);
            chatBox.removeChild(loadingIndicator);
        });
});
