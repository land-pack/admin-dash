from core import db
from core.models import User
from werkzeug.security import generate_password_hash

if __name__ == '__main__':

    login = 'frank'
    passwd = generate_password_hash('openos')
    u = User(login='frank', password=passwd)
    db.session.add(u)
    db.session.commit()
