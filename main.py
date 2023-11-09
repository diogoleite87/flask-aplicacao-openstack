# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

usuarios = []


@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Minha Página Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                margin: 100px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <h1>Olá, Mundo!</h1>
        <p>Esta é uma página bonita em Flask.</p>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
