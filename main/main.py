from flask import Flask
from models import db  # This should include your Product & ProductUser models
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Optional: Just to check it works
@app.route('/')
def index():
    return "Hello Flask"
