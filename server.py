import bcrypt
import random
import string

from flask import Flask, request
app = Flask(__name__)

def get_random_str(length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))

@app.route('/bcrypt')
def encrypt():
    work_factor = int(request.args.get('work_factor', 12))
    password_length = int(request.args.get('password_length', 20))
    password  = request.args.get('password', get_random_str(password_length))

    return bcrypt.hashpw(password, bcrypt.gensalt(rounds=work_factor))
