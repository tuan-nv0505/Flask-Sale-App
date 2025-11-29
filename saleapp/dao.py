from saleapp.models import Category, Product, User
from hashlib import md5

def load_categories():
    return Category.query.all()

def load_products(category_id=None, kw=None, page=1):
    query = Product.query

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.all()

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    password = str(md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username==username, User.password==password).first()
