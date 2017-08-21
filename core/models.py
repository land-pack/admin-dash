from core import db


# Create user model.
class User(db.Model):
    __tablename__ = 't_agent_manager'
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
    __tablename__ = 't_agent_user'
    f_id = db.Column(db.Integer, primary_key=True)
    f_username = db.Column(db.String(64))
    f_idcard = db.Column(db.String(18), unique=True)
    f_mobile = db.Column(db.String(11), unique=True)
    f_alipay = db.Column(db.String(64))
    f_qq = db.Column(db.String(16))
    f_status = db.Column(db.Integer)
    f_verify = db.Column(db.Integer)
    f_relate_uid = db.Column(db.BIGINT)
    f_regtime = db.Column(db.TIMESTAMP)
    f_passwd = db.Column(db.String(128))
    f_share_url = db.Column(db.String(128))
    f_share_code = db.Column(db.String(32), unique=True)
    f_refound = db.Column(db.Integer)
    f_refound_done = db.Column(db.Integer)
    f_refound_status = db.Column(db.Integer)
    # Required for administrative interface
    def __unicode__(self):
        return self.f_idcard


# Create user model.
class RechargeManager(db.Model):
    __tablename__ = 't_agent_player_log'


    f_id = db.Column(db.Integer, primary_key=True)
    f_crtime = db.Column(db.TIMESTAMP)
    f_agent_code = db.Column(db.String(64))
    f_invitee = db.Column(db.BIGINT)
    f_recharge = db.Column(db.BIGINT)
    f_place = db.Column(db.BIGINT)
    f_prize = db.Column(db.BIGINT)
    f_prate = db.Column(db.FLOAT)
    f_tax = db.Column(db.BIGINT)
    f_cost = db.Column(db.BIGINT)
    f_profit = db.Column(db.BIGINT)
    
        # Required for administrative interface
    def __unicode__(self):
        return self.f_id

# class PlayerDailyLog(db.Model):

