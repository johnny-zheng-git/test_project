from .. import db
from sqlalchemy import Integer, String


class User_zwq(db.Model):  # 继承declarative_base类
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    username = db.Column(String(32), nullable=False)
    pwd = db.Column(String(64), nullable=False)