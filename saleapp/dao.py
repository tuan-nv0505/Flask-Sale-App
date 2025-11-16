from saleapp.models import Category, Product, User

def load_category():
    return Category.query.all()

def load_product(category_id=None, kw=None, page=1):
    query = Product.query

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.all()

def get_user_by_id(id):
    return User.query.get(id)