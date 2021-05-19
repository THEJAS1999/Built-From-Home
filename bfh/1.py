from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

users = [{'uid': 1, 'name': 'Noah Schairer'}]

# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)

    

@app.route("/")
def userinfo():
    return {'data': users}, 200
# def index():
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)