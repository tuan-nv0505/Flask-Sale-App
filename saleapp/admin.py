from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product, UserRole
from saleapp import db, app
from flask_login import current_user

class AdminView(ModelView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class ProductView(AdminView):
    column_list = ['id', 'name', 'price', 'active', 'category_id', 'category']
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    can_export = True
    edit_modal = True
    column_editable_list = ['name', 'price']
    page_size = 10

admin = Admin(app=app, name="e-Commerce's Admin")
admin.add_view(AdminView(Category, db.session))
admin.add_view(ProductView(Product, db.session))