from flask import Flask, request, jsonify
import bcrypt
import sqlite3

app = Flask(__name__)

DATABASE = 'users.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Login e senha são campos obrigatórios.'}), 400

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (login, password_hash) VALUES (?, ?)', (login, password_hash))
    conn.commit()

    return jsonify({'message': 'Usuário criado com sucesso.'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Login e senha são campos obrigatórios.'}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
    user = cursor.fetchone()

    if not user:
        return jsonify({'error': 'Usuário não encontrado.'}), 401

    try:
        if bcrypt.checkpw(password.encode('utf-8'), user[2]):
            return jsonify({'message': 'Login bem-sucedido.'}), 200
        else:
            return jsonify({'error': 'Credenciais inválidas.'}), 401
    except bcrypt.BcryptError:
        return jsonify({'error': 'Erro ao verificar a senha.'}), 500
    
if __name__ == '__main__':
    init_db()
    app.run()