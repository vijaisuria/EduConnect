from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
import sqlite3
from extensions import mail
from flask_cors import CORS

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False

mail.init_app(app)
jwt = JWTManager(app)

# Database setup
conn = sqlite3.connect('database.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL, verified BOOLEAN DEFAULT 0)')
conn.commit()

from routes.auth_routes import auth_routes
from routes.course_routes import course_routes

@app.route('/', methods=['GET'])
def index():
    token = session.get('token')
    if token:
        try:
            decoded_token = decode_token(token)
            uid = decoded_token.get('sub')
            return render_template('chat.html', token=uid)
        except jwt.ExpiredSignatureError:
            return render_template('auth.html')
    return render_template('auth.html')

@app.route('/account', methods=['GET'])
def auth():
    return render_template('auth.html')

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(course_routes, url_prefix='/course')


@app.route('/chat')
def chat():
    token = request.args.get('token')
    if not token:
        return jsonify({'message': 'Token is missing.'}), 400
    
    decoded_token = decode_token(token)
    id = decoded_token['sub']
    return render_template('chat.html', token=id)

@app.route('/users', methods=['GET'])
def get_users():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    users_data = []
    for user in users:
        user_data = {
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'verified': user[4]
        }
        users_data.append(user_data)
    return jsonify(users_data), 200

if __name__ == '__main__':
    app.run(debug=True)
