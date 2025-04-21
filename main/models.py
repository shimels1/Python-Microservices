# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Product id={self.id}, title='{self.title}'>"


class ProductUser(db.Model):
    __tablename__ = 'product_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(200), nullable=False)
    product_id = db.Column(db.String(200), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'product_id', name='user_product_unique'),
    )

    def __repr__(self):
        return f"<ProductUser user_id={self.user_id}, product_id={self.product_id}>"
