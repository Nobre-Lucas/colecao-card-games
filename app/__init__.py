from flask import Flask


print(__name__)
app = Flask(__name__)


from app.controllers import index, login, signup