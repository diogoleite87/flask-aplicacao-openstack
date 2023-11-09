# -*- coding: utf-8 -*-
from flask import Flask, request
import logging

app = Flask(__name__)

usuarios = []

# Configuração de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/')
def hello_world():
    # Obtém o endereço IP do usuário
    user_ip = request.remote_addr

    # Verifica se o IP do usuário já está na lista de usuários
    if user_ip not in usuarios:
        usuarios.append(user_ip)
        # Registra a conexão do usuário no log
        logging.info(f'Novo usuário conectado: {user_ip}')

    # Retorna a página HTML
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Minha Página Flask</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                margin: 100px;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                font-size: 18px;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <h1>Olá, Mundo!</h1>
        <p>Usuários conectados: {len(usuarios)}</p>
        <p>IPs dos usuários: {', '.join(usuarios)}</p>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
