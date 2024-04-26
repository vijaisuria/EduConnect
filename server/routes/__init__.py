from .auth_routes import auth_routes
from .course_routes import course_routes
from .educonnect import educonnect_bp

# Optionally, you can define a function to initialize all the Blueprints
def init_app(app):
    app.register_blueprint(auth_routes, url_prefix='/auth')
    app.register_blueprint(course_routes, url_prefix='/course')
    app.register_blueprint(educonnect_bp, url_prefix='/educonnect')


