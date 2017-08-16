from core import db


# Create user model.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username



# Create user model.
class Agenter(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    f_username = db.Column(db.String(100))
    f_idcard = db.Column(db.String(128))
    f_mobile = db.Column(db.String(80), unique=True)
    f_alipay = db.Column(db.String(120))
    f_qq = db.Column(db.String(64))
    f_status = db.Column(db.Integer)
    f_verify = db.Column(db.Integer)
    f_relate_uid = db.Column(db.Integer)
    f_regtime = db.Column(db.Date)
    f_passwd = db.Column(db.String(256))
    f_share_url = db.Column(db.String(128))
    f_share_code = db.Column(db.String(128))

