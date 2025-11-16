from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '$%#$%7389h$&nj:ab-09;j28835$#G$g4g$egg@@444ajd'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:tuannv0505@localhost/saleappdb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)