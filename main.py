from flask import Flask, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'API funcionando no Cloud Run!',
        'timestamp': datetime.now().isoformat(),
        'service': 'minha-api-cloud-run'
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    # Simulando uma lista de usuários
    usuarios = [
        {'id': 1, 'nome': 'João', 'email': 'joao@email.com'},
        {'id': 2, 'nome': 'Maria', 'email': 'maria@email.com'},
        {'id': 3, 'nome': 'Pedro', 'email': 'pedro@email.com'}
    ]
    return jsonify({
        'usuarios': usuarios,
        'total': len(usuarios)
    })

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'erro': 'Nome e email são obrigatórios'}), 400
    
    # Simulando criação de usuário
    novo_usuario = {
        'id': 4,
        'nome': dados['nome'],
        'email': dados['email'],
        'criado_em': datetime.now().isoformat()
    }
    
    return jsonify({
        'mensagem': 'Usuário criado com sucesso',
        'usuario': novo_usuario
    }), 201

@app.route('/info')
def info():
    return jsonify({
        'service_name': os.environ.get('K_SERVICE', 'local'),
        'service_version': os.environ.get('K_REVISION', 'local'),
        'port': os.environ.get('PORT', '8080'),
        'project': os.environ.get('GOOGLE_CLOUD_PROJECT', 'local')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)