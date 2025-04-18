from flask import Flask 
def create_app():
    app = Flask(__name__, template_folder='templates')

    return app

app = create_app()

from applications.route import *
if __name__ == '__main__':
    

    app.run(debug=True)
