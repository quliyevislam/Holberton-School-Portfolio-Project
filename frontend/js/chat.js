// AI Chat button functionality
const chatOverlay = document.getElementById('chat-overlay');
const closeChatButton = document.querySelector('.close-chat'); // Updated selector
const aiChatButton = document.getElementById('ai-chat-button');
const chatBox = document.querySelector('.chat-box');
const sendButton = document.querySelector('.send-button');
const inputField = document.querySelector('.input-field');

aiChatButton.addEventListener('click', () => {
  chatOverlay.style.display = 'flex';
});

closeChatButton.addEventListener('click', () => {
  chatOverlay.style.display = 'none';
});

sendButton.addEventListener('click', () => {
  const userInput = inputField.value.trim();

  if (!userInput) {
    return;
  }

  const jsonData = { message: userInput };
  inputField.value = '';

  const userMessage = document.createElement('div');
  const pUser = document.createElement('p');

  userMessage.classList.add('chat-message', 'user-message');
  userMessage.appendChild(pUser);
  pUser.textContent = userInput;
  chatBox.appendChild(userMessage);

  const loadingIndicator = document.createElement('div');
  loadingIndicator.classList.add('loading-indicator');
  chatBox.appendChild(loadingIndicator);

  chatBox.scrollTop = chatBox.scrollHeight;

  fetch('http://0.0.0.0:5000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(jsonData),
  })
    .then((response) => response.json())
    .then((result) => {
      chatBox.removeChild(loadingIndicator);

      const aiMessage = document.createElement('div');
      const pAi = document.createElement('p');

      aiMessage.classList.add('chat-message', 'ai-message');
      aiMessage.appendChild(pAi);

      result = result.replaceAll('**', '<br>').replaceAll('*', '');
      pAi.innerHTML = result;
      chatBox.appendChild(aiMessage);

      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch((error) => {
      console.error('Error:', error);
      chatBox.removeChild(loadingIndicator);
    });
});