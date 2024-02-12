from flask_sqlalchemy import SQLAlchemy, DateTime
from sqlalchemy.sql import func

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
# connect_db(postDB)
    
class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.String(200), nullable=True)

class Post(db.Model):
    "Post."

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    content = db.Column(db.String(200),
                     nullable=False,
                     unique=True)
    created_at = db.Column(DateTime, default=func.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post id={self.id}, title={self.title}, content={self.content}, created_at={self.created_at}>"

    # def save(user_id):
    #     return 