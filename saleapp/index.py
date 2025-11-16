from pathlib import Path
import sys
ROOT_DIR = Path(__name__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from saleapp import app, dao, login
from flask import render_template, request


@app.route('/')
def index():
    category = dao.load_category()
    products = dao.load_product(
        category_id=request.args.get('category_id'),
        kw=request.args.get('kw'),
        page=request.args.get('page')
    )

    return render_template('index.html', category=category, products=products)

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

if __name__ == '__main__':
    from saleapp import admin
    app.run(debug=True)
