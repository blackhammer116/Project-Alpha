from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
DB_NAME = "fullstack"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fullstack.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/' + DB_NAME
    db.init_app(app)

    from webflask.views import views
    from webflask.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from webflask.models import User, Note
    
    with app.app_context():
        db.create_all()
        print('Created Database!')

        # Create an admin user if not already present
        admin_user = User.query.filter_by(username='admin').first()
        password_hash = generate_password_hash('admin_password', method='scrypt')

        if not admin_user:
            admin_user = User(
                username='admin',
                email='admin@example.com',
                password=password_hash,
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print('Admin Created!')
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.session_protection ='strong'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

