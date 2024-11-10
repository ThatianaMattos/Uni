import requests

# Substitua com sua chave de API do Google Gemini
api_key = 'AIzaSyAt8E8joWCKero1qnZTznKwALWWNSXxsKQ'
api_endpoint = 'https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText'

def ask_gemini(question):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        'prompt': {
            'text': question
        },
        'maxOutputTokens': 150
    }
    
    response = requests.post(api_endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['candidates'][0]['output']
    else:
        return f"Erro: {response.status_code} - {response.text}"
