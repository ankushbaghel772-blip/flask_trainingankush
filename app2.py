```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL connection using PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:YOUR_PASSWORD@localhost/flask_project'
)
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


@app.route("/")
def home():
    return "<h1>Hello, Ankush Baghel</h1>"


if __name__ == "__main__":
    app.run(debug=True)
```
