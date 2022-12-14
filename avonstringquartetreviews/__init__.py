import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
DATABASE = "avonSQReviews"
COLLECTION = "users"

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    print(uri)
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)
mongo = PyMongo(app)
migrate = Migrate(app, db)

from avonstringquartetreviews import routes  # noqa
