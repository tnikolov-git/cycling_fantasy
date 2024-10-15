from Flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py')

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app