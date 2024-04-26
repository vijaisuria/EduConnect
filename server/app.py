from flask import Flask, request, jsonify, render_template, session, url_for, redirect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
import sqlite3
from extensions import mail
from flask_cors import CORS
import json

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
from routes.enrollment_routes import enrollment_routes
from routes.educonnect import educonnect_bp 
from routes.learn_route import learn_route

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('educonnect.index'))

@app.route('/account', methods=['GET'])
def auth():
    return render_template('auth.html')

app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(enrollment_routes, url_prefix='/enrollment')
app.register_blueprint(educonnect_bp, url_prefix='/educonnect')
app.register_blueprint(learn_route, url_prefix='/learn')

@app.route('/chat')
def chat():
    token = session.get('token')

    decoded_token = decode_token(token)
    uid = decoded_token.get('sub')
    return render_template('peers.html', token=uid)

@app.route('/get_exams')
def get_exams():
   with open('static/data/exams.json', 'r') as file:
        data = json.load(file)
        return data

if __name__ == '__main__':
    app.run(debug=True)
