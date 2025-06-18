from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.auth import auth_bp
    from .routes.materia import materia_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(materia_bp)  


    
    return app