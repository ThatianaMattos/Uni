import os
import google.generativeai as gemini

# Configure sua variável de ambiente com o caminho para o arquivo JSON de credenciais
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

class GeminiService:
    def __init__(self):
        # Inicialize a API com sua chave de API do Google Generative AI (Gemini)
        gemini.configure(api_key="your-api-key")

    def get_response(self, prompt):
        # Envia um prompt para a API do Gemini e retorna a resposta
        response = gemini.generate_text(prompt=prompt)
        return response['candidates'][0]['output']


# from google.cloud import dialogflow_v2 as dialogflow
# import os

# # Configure sua variável de ambiente com o caminho para o arquivo JSON de credenciais
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"
# class GeminiService:
#     def __init__(self):
#         # Inicialize aqui a conexão com a API do Google Gemini
#         pass

#     def get_response(self, prompt):
#         # Implemente aqui a lógica para enviar prompts à API do Google Gemini e retornar a resposta
#         pass
