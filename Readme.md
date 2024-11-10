
# Projeto Uni1500 - Chatbot

![Chatbot Uni1500](app/static/images/ChatBot.jpg)

Este é o projeto do chatbot desenvolvido como parte do curso Uni1500. Ele foi projetado para simular um assistente virtual com funcionalidades de interação e gerenciamento, utilizando tecnologias modernas para frontend, backend e banco de dados.

## Estrutura do Projeto

A estrutura do projeto foi organizada da seguinte forma:

- **app**: Contém a lógica principal da aplicação e a comunicação com o backend.
  - **services**: Scripts de serviço para funções específicas, como `chat_service.py`, `db_service.py`, e `gemini_service.py`, que gerenciam a interação com a base de dados e funções do chatbot.
  - **static**: Diretório com arquivos estáticos, incluindo imagens e arquivos CSS.
    - **images**: Contém imagens utilizadas no projeto, como o logo do chatbot.
    - **css**: Arquivos de estilização, como `chat.css`, `login.css`, e `register.css`, que definem o design da aplicação.
  - **templates**: Diretório para os templates HTML do projeto.
  - **routes.py**: Arquivo que define as rotas da aplicação, facilitando a navegação entre as páginas.

- **venv**: Ambiente virtual onde estão instaladas as dependências do projeto, listadas em `requirements.txt`.

- **BD.sql**: Script para configuração do banco de dados utilizado pelo projeto.

## Funcionalidades

1. **Autenticação de Usuário**: Inclui telas de login e registro, com proteção para acesso seguro ao chatbot.
2. **Interação com o Chatbot**: Interface para o usuário interagir com o assistente virtual, com funcionalidades específicas de resposta e suporte.
3. **Integração com Banco de Dados**: Gerenciamento de dados estruturados e não estruturados, integrados com MySQL para armazenamento seguro das informações.
4. **Design Personalizado**: Estilos personalizados aplicados nas telas para criar uma experiência amigável e visualmente atraente.
5. **Modularidade**: Separação de responsabilidades com arquivos de serviço, facilitando manutenção e expansão do projeto.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, com bibliotecas e frameworks como Flask e FastAPI
- **Banco de Dados**: MySQL para armazenamento estruturado de dados
- **Ambiente Virtual**: Configurado com `requirements.txt` para fácil instalação das dependências

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd Uni1500
   ```

3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure o banco de dados usando o script `BD.sql`.

6. Execute o servidor:
   ```bash
   python app/main.py
   ```

7. Abra o navegador e acesse `http://localhost:5000` para visualizar o projeto.
