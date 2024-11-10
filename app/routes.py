from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from .gemini_service import GeminiService
from flask import flash
from flask_mysqldb import MySQL
from app import mysql
import os
import mysql.connector
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

bp = Blueprint('main', __name__)

# Configuração da chave de API do Google
google_api_key = 'AIzaSyAt8E8joWCKero1qnZTznKwALWWNSXxsKQ'
os.environ["GOOGLE_API_KEY"] = google_api_key

memory = ConversationBufferMemory()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Configuração da conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': 'Uni1500'
}
chat_bp = Blueprint('chat', __name__)
gemini_service = GeminiService()

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data['message']
    session_id = 'unique-session-id'  # Você pode gerar um ID de sessão exclusivo por usuário

    response = gemini_service.get_response(session_id, user_message)
    return jsonify({'response': response})

# Verificando se a variável está sendo acessada corretamente
print(f"Senha do MySQL: {os.getenv('MYSQL_PASSWORD')}")

@bp.route('/', methods=['GET'])
def home():
    if 'user' in session:
        return redirect(url_for('main.chat'))
    return redirect(url_for('main.login'))

@bp.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.json.get('message')

        if not user_message:
            return jsonify({'error': 'Mensagem ausente.'}), 400

        # Detecção de palavras-chave como "vendedores" e "base de dados"
        if "vendedores" in user_message.lower() and "base de dados" in user_message.lower():
            return query_vendedores()

        # Verificar se o usuário forneceu detalhes suficientes para uma resposta adequada
        if len(user_message.split()) < 5:  # Exemplo de detecção de mensagem genérica
            return ask_generic_question(user_message)

        # Continuar com a lógica normal de chatbot
        context = f"Usuário: {user_message}\n"
        messages = [
            ("system", "Você é um assistente vencedor e seu objetivo é ajudar o usuário da forma mais eficiente possível."),
            ("human", context.strip())
        ]

        ai_msg = llm.invoke(messages)
        context += f"Assistente: {ai_msg.content}\n"

        return jsonify({'response': ai_msg.content})

    except Exception as e:
        # Capture o erro e retorne uma resposta mais detalhada
        return jsonify({'error': str(e)}), 500


# Função para lidar com perguntas genéricas
def ask_generic_question(user_message):
    generic_responses = [
        "Você poderia fornecer mais detalhes sobre o que exatamente está procurando?",
        "Poderia me dar mais informações para te ajudar melhor?",
        "Posso te ajudar com algo específico, como vendedores, produtos, ou outra coisa?"
    ]
    
    response = generic_responses[len(user_message) % len(generic_responses)]  # Seleciona uma resposta com base no tamanho da mensagem
    
    return jsonify({'response': response})

# Função para consulta de vendedores
def query_vendedores():
    try:
        # Conectando ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Consulta para buscar vendedores (ajustar de acordo com sua estrutura)
        query = "SELECT nome_vendedor, email FROM vendedores"
        cursor.execute(query)
        result = cursor.fetchall()

        # Formatando o resultado
        response = "Aqui estão seus vendedores:\n"
        for row in result:
            response += f"Nome: {row[0]}, Email: {row[1]}\n"

        cursor.close()
        conn.close()

        return jsonify({'response': response})

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

@bp.route('/query_sql', methods=['POST'])
def query_sql():
    user_query = request.json.get('query')

    if not user_query:
        return jsonify({'error': 'Consulta SQL ausente.'}), 400

    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Consulta SQL segura
        sql_safe_query = "SELECT * FROM inseminacao WHERE fazenda LIKE %s"
        param = ("%" + user_query + "%",)  # Evitar SQL Injection

        cursor.execute(sql_safe_query, param)
        result = cursor.fetchall()

        # Formatando o resultado
        columns = [desc[0] for desc in cursor.description]
        result_data = [dict(zip(columns, row)) for row in result]

        cursor.close()
        conn.close()

        if result_data:
            return jsonify({'result': result_data})
        else:
            return jsonify({'message': 'Nenhum dado encontrado.'})

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session['user'] = email
        return redirect(url_for('main.chat'))
    return render_template('login.html')

@bp.route('/chat')
def chat():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    return render_template('chat.html')

@bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.login'))

@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('forgot_password.html', message="Se um usuário com este email existir, enviaremos instruções de recuperação.")
    return render_template('forgot_password.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return render_template('register.html', message="Cadastro realizado com sucesso. Faça login.")
    return render_template('register.html')
from flask import Flask, request, jsonify
from db_service import get_inseminacao_by_fazenda

@app.route('/consultar_inseminacao', methods=['POST'])
def consultar_inseminacao():
    nome_fazenda = request.json.get('nome_fazenda')
    resultados = get_inseminacao_by_fazenda(nome_fazenda)
    return jsonify(resultados)
def fetch_insemination_data(nome_fazenda=None):
    cursor = mysql.connection.cursor()
    
    if nome_fazenda:
        query = "SELECT * FROM inseminacao WHERE fazenda = %s"
        cursor.execute(query, (nome_fazenda,))
    else:
        query = "SELECT * FROM inseminacao"
        cursor.execute(query)
    
    records = cursor.fetchall()
    db_info = "\n".join([f"ID: {row[0]}, Data: {row[1]}, Valor: {row[2]}, Fazenda: {row[3]}" for row in records])
    cursor.close()
    return db_info
    
    from flask import Flask, jsonify
from db_service import fetch_insemination_data

@app.route('/get_insemination_data', methods=['GET'])
def get_insemination_data():
    # Busca todos os registros
    data = fetch_insemination_data()

    return jsonify({'data': data})

@app.route('/get_insemination_data/<nome_fazenda>', methods=['GET'])
def get_insemination_data_for_fazenda(nome_fazenda):
    # Busca registros para uma fazenda específica
    data = fetch_insemination_data(nome_fazenda)

    return jsonify({'data': data})
