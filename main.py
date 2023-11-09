from flask import Flask, request

app = Flask(__name__)

# Lista para rastrear os IPs dos usuários
usuarios = []


@app.route('/')
def hello_world():
    # Obtém o IP do usuário atual
    ip = request.remote_addr

    # Adiciona o IP à lista se ainda não estiver lá
    if ip not in usuarios:
        usuarios.append(ip)

    return f'IP da Máquina: {request.host}, Porta: {request.environ["SERVER_PORT"]}, Total de Usuários: {len(usuarios)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
