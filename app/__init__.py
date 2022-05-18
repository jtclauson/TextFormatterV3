from flask import Flask

app = Flask(__name__)
app.secret_key = "kagi"
from app.scripts import routes