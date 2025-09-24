
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Olá, Mundo! Imagem Docker publicada com sucesso via GitHub Actions!</h1>'

if __name__ == '_main_':
    
    app.run(host='0.0.0.0', port=5000)
