#!/usr/bin/env python3
from werkzeug.security import generate_password_hash
from webflask import create_app, db
from webflask.models import User

# Generate password hash
password_hash = generate_password_hash('admin_password', method='scrypt')

app = create_app()
app.app_context().push()

admin = User(
    username='Admin',
    email='admin@example.com',
    password=password_hash,
    is_admin=True
)

with app.app_context():
    db.session.add(admin)
    db.session.commit()
    print('Admin Created!')
