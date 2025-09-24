from flask import Flask
from routes import init_routes
from database import init_db
from config import DATABASE_URI, SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY

    init_db(app)
    init_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
