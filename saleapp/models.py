from saleapp import db, app
from sqlalchemy import Column, Integer, String, Boolean, Text, Float, ForeignKey, Enum, inspect
from sqlalchemy.orm import relationship
from enum import Enum as UserEnum
from flask_login import UserMixin
import hashlib

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    avatar = Column(String(255), default='https://wandermind.ai/wp-content/uploads/2024/02/DALL%C2%B7E-2024-02-27-15.33.42-Imagine-a-cartoon-style-image-of-a-greedy-robot.-This-robot-is-designed-with-exaggerated-features-to-highlight-its-greediness.-It-has-large-glowing-e.webp')
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = Column(String(50), unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg")
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        #
        # user = User(name='Admin', username='admin', password=str(hashlib.md5('admin@12345'.encode('utf-8')).hexdigest()), user_role=UserRole.ADMIN)
        # db.session.add(user)

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        # db.session.add_all([c1, c2, c3])

        # products = [
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        #     {
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824106/ipad_pro_2020_tr3llb.jpg",
        #         "category_id": 2
        #     },
        #     {
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAM: 6GB",
        #         "price": 24000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/galaxy_note_10_yrmuxs.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Iphone 12 pro",
        #         "description": "Apple, 64GB, RAM: 6GB",
        #         "price": 34000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763823331/iphone_12_lgokqu.jpg",
        #         "category_id": 1
        #     },
        #     {
        #         "name": "Macbook Pro M4",
        #         "description": "Macbook, 128GB Memory, 2048GB SSD",
        #         "price": 240000000,
        #         "image": "https://res.cloudinary.com/dt1pa28g2/image/upload/v1763824679/mac_pro_m4_vhhkrf.jpg",
        #         "category_id": 3
        #     },
        # ]
        #
        # for p in products:
        #     product = Product(**p)
        #     db.session.add(product)
        db.session.commit()