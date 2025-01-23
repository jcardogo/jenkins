#This is not an executable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hola_mundo(name):
    return f'Hola, {name}!'