document.getElementById("user-input").addEventListener("input", function () {
  const message = this.value.trim();
  toggleSendButton(message.length > 0);
});

/// Respostas aleatórias para simular a IA
const responses = [
  "Claro, posso te ajudar com isso!",
  "Desculpe, você pode repetir a pergunta?",
  "Interessante, me conte mais!",
  "Estou aqui para ajudar!",
  "Essa é uma ótima pergunta!",
  "Deixe-me pensar...",
  "Posso procurar isso para você.",
  "Não tenho certeza, mas posso descobrir!",
  "Isso parece complicado, vamos resolver juntos.",
  "Você pode tentar reformular a questão?",
];

// Função para enviar uma mensagem
function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();

  if (message) {
    // Adiciona a mensagem do usuário no chat
    addMessageToChat(message, "user");

    // Limpa o campo de entrada
    userInput.value = "";

    // Envia a mensagem para o servidor Flask e obtém a resposta da IA
    fetch("/send_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Adiciona a resposta da IA ao chat
        addMessageToChat(data.response, "ia");
      })
      .catch((error) => {
        console.error("Error:", error);
        addMessageToChat("Erro ao obter resposta da IA.", "ia");
      });
  }
}

// Função para adicionar uma mensagem ao chat
function addMessageToChat(message, sender) {
  const chatWindow = document.querySelector(".chat-window");
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", sender);

  const bubbleElement = document.createElement("div");
  bubbleElement.classList.add("bubble");
  bubbleElement.textContent = message;

  messageElement.appendChild(bubbleElement);
  chatWindow.appendChild(messageElement);

  // Rolagem automática para a última mensagem
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Função para obter uma resposta aleatória
function getRandomResponse() {
  const randomIndex = Math.floor(Math.random() * responses.length);
  return responses[randomIndex];
}

// Função para habilitar/desabilitar o botão de enviar
function toggleSendButton(enable) {
  const sendButton = document.querySelector(".input-area button");
  sendButton.disabled = !enable;
}
function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();

  if (message) {
    addMessageToChat(message, "user");
    userInput.value = "";
    toggleSendButton(false);

    addMessageToChat("Aguardando resposta...", "ia");

    fetch("/send_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        const chatWindow = document.querySelector(".chat-window");
        chatWindow.lastElementChild.textContent = data.response;
        toggleSendButton(true);
      })
      .catch((error) => {
        console.error("Error:", error);
        const chatWindow = document.querySelector(".chat-window");
        chatWindow.lastElementChild.textContent =
          "Erro ao obter resposta da IA.";
        toggleSendButton(true);
      });
  }
}
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("hidden");
}
// Função para enviar uma mensagem
function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();

    if (message) {
        addMessageToChat(message, "user");

        userInput.value = "";

        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            addMessageToChat(data.response, "ia");
        })
        .catch(error => {
            console.error('Error:', error);
            addMessageToChat("Erro ao obter resposta da IA.", "ia");
        });
    }
}

// Função para adicionar uma mensagem ao chat
function addMessageToChat(message, sender) {
    const chatWindow = document.querySelector(".chat-window");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);

    const bubbleElement = document.createElement("div");
    bubbleElement.classList.add("bubble");
    bubbleElement.textContent = message;

    messageElement.appendChild(bubbleElement);
    chatWindow.appendChild(messageElement);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Função para habilitar/desabilitar o botão de enviar
function toggleSendButton(enable) {
    const sendButton = document.querySelector(".input-area button");
    sendButton.disabled = !enable;
}
