from flask import Flask

#create a flask application called app 
app = Flask(__name__)


#define the root/starting point 
@app.route('/')
def hello_world():
    return 'Hello world'

    