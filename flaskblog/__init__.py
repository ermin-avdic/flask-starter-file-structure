from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = ""
app.config["SQLALCHEMY_DATABASE_URI"] = ""

from flaskblog import routes