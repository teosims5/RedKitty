from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

app.run()

def apprun ():
    if __name__ == '__main__':
        app.run()
        
apprun()
