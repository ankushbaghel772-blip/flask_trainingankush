from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/flask_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print("ankush baghel")

db = SQLAlchemy(app)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    phone_num = db.Column(db.String(80), nullable=True)
    meg = db.Column(db.String(80), nullable=True)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)