# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

usuarios = []


@app.route('/')
def hello_world():
    ip = request.remote_addr

    if ip not in usuarios:
        usuarios.append(ip)

    return f'IP da Maquina: {request.host}, Porta: {request.environ["SERVER_PORT"]}, Total de Usuarios: {len(usuarios)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
