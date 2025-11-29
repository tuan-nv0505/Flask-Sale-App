from pathlib import Path
import sys
ROOT_DIR = Path(__name__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app, dao, login
from flask import render_template, request, redirect
from flask_login import login_user


@app.route('/')
def index():
    products = dao.load_products(
        category_id=request.args.get('category_id'),
        kw=request.args.get('kw'),
        page=request.args.get('page')
    )

    return render_template('index.html', products=products)

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

@app.route('/login', methods=['post'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    next = request.args.get('next')
    return redirect(next if next else '/admin')

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.context_processor
def common_responses():
    return {
        'categories': dao.load_categories()
    }

if __name__ == '__main__':
    from saleapp import admin
    app.run(debug=True)
