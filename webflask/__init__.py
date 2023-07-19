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

    from webflask.models import User, Note, Service

    with app.app_context():
        db.create_all()
        print('Created Database!')

        # Create services
        services = [
            Service(name='Computer pen test'),
            Service(name='Server pen test'),
            Service(name='Android pen test'),
            Service(name='Network scan'),
            Service(name='Web application security testing')
        ]

        existing_service_names = [
            service.name for service in Service.query.all()]
        new_services = [
            service for service in services if service.name not in existing_service_names]

        if new_services:
            db.session.bulk_save_objects(services)
            db.session.commit()
            print('Services Created!')
        else:
            print('No new services to create.')

        # Create an admin user if not already present
        admin_user = User.query.filter_by(username='Admin').first()
        password_hash = generate_password_hash(
            'admin_password', method='scrypt')

        if not admin_user:
            admin_user = User(
                username='Admin',
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
    login_manager.session_protection = 'strong'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
