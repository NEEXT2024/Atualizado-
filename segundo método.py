import requests

# URL do script no GitHub
url = 'https://raw.githubusercontent.com/NEEXT2024/pk/main/m%C3%A9todo%20neext%20criptografado.py'

# Adicione seu token de autenticação se necessário
headers = {
    'Authorization': 'token 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'
}

try:
    # Fazendo a requisição para obter o conteúdo do script
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição

    # Obter o conteúdo do script como texto
    script_content = response.text

    # Executar o script
    exec(script_content)

except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar o script: {e}')
except Exception as e:
    print(f'Erro ao executar o script: {e}')