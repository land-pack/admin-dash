from flask import render_template, flash, redirect, url_for, session, g, request
from core import app
from core import lm
from core import oid
from core import db
from flask_admin.contrib import sqla
import flask_login as login
import flask_admin as admin
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegistrationForm
from .models import User, Agenter


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + \
            url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + \
            url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


class AgentView(MyModelView):
    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True
    can_export = True

    column_exclude_list = ['f_passwd', 'f_share_url']
    column_searchable_list = ['f_mobile', 'f_share_code']
    column_editable_list = ['f_verify', "f_relate_uid"]

    # the different between form_choices and column_choices
    column_choices = {
        'f_verify': [
            (1, 'Checking'),
            (-1, 'Rejected'),
            (0, 'Pass')
        ]
    }

    form_choices = {
        "f_verify": [
            ("Checking", "Checking"),
            ("Recjected", "Recjected"),
            ("Pass", "Pass")

        ]

    }

    column_descriptions = {
    	"f_username":'First name and last name'
    }

    column_labels = dict(f_username='Username', 
    					f_idcard='IDCard',
    					f_mobile='Mobile',
    					f_alipay='Alipay',
    					f_qq='QQ',
    					f_status='Status',
    					f_verify='Verify',
    					f_relate_uid='UID',
    					f_regtime='Regtime',
    					f_share_code='Code'
    					)


 #    form_widget_args = {
 #    'f_verify': {
 #        'rows': 7,
 #        'style': 'color: red'
 #    	}
	# }

# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Create admin
admin = admin.Admin(app, 'Agent Dash', index_view=MyAdminIndexView(
), base_template='my_master.html')

# Add view
admin.add_view(MyModelView(User, db.session))
admin.add_view(AgentView(Agenter, db.session))
