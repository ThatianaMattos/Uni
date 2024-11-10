function togglePassword() {
    const passwordField = document.getElementById('password'); // Ajuste o ID conforme necessário
    const toggleButton = document.getElementById('togglePassword');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    toggleButton.innerHTML = type === 'password' ? 'Mostrar' : 'Ocultar';
}

// Adiciona um evento para alternar a visibilidade da senha ao clicar no botão
document.getElementById('togglePassword').addEventListener('click', togglePassword);
