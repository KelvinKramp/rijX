from flask_admin import Admin, expose
from flask_admin import helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, Security, SQLAlchemyUserDatastore
from flask import render_template, url_for,  redirect
from forms import UserInfoForm, LocationDateForm, ScheduleForm, CancellationForm, SearchForm
from flask import request, session
from flask_sqlalchemy import SQLAlchemy
from helpers.mail import send_message_mailgun as send_mail
from datetime import datetime as dt
from datetime import timezone
from planningOS import create_slots, create_appointment, get_from_db, cancel, delete_rows
from app import secureApp, db, Users, Roles, Slots, app
from datetime import datetime as dt
from datetime import timezone
from planningOS import create_slots, create_appointment, get_ninja_tables
import requests
import numpy as np
from definitions import nav_bar_items
from texts import texts_landingpage

# Create a ModelView to add to our administrative interface
class UserModelView(ModelView):
    # Override the is_accessible method from ModelView and only return True if user is active and authenticated
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

    # Only return navigation menu for users that are logged in and set on active
    # When an not logged in and inactive individual goes to www.website.com/admin/users the
    # login page will be returned
    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

class AppointmentsView(UserModelView):
    @expose("/", methods=['GET', 'POST'])
    def index(self):
        html_table_slots = get_from_db(form='html', var='openslots')
        html_table_appointments = get_from_db(form='html',var='appointments')
        html_table_workers = get_from_db(form='html',var='workers')
        headings = ["Open slots", "Appointments", "Workers"]
        tables = [html_table_slots, html_table_appointments, html_table_workers]
        table_ninja_clean = {}
        tables_ninja = []
        for i, j in enumerate(tables):
            table_ninja = table_ninja_clean.copy()
            table_ninja.clear()
            table_ninja["heading"] = headings[i].capitalize()
            table_ninja["table"] = j
            tables_ninja.append(table_ninja)
        return self.render('admin/appointments.html', tables_ninja=tables_ninja)


class OpenSlotsView(UserModelView):
    @expose("/", methods=['GET', 'POST'])
    def index(self):
        tables_ninja = get_ninja_tables()
        return self.render('admin/openslots.html', tables_ninja=tables_ninja)

class ScheduleView(UserModelView):
    @expose("/", methods=['GET', 'POST'])
    def index(self):
        form = ScheduleForm()
        # print(form.errors)
        location = form.location.data
        date = form.date.data
        starttime = form.starttime.data
        endtime = form.endtime.data
        if form.timeduration.data:
            timeduration = int(form.timeduration.data[0:2])
        worker = form.worker.data
        if form.validate_on_submit():
            create_slots(location, date, starttime, endtime, timeduration, worker)
            tables_ninja = get_ninja_tables()
            return self.render('admin/openslots.html', tables_ninja=tables_ninja)
        return self.render('admin/schedule.html', form=form)


class CancellationView(UserModelView):
    @expose("/", methods=['GET', 'POST'])
    # https://stackoverflow.com/questions/45877080/how-to-create-dropdown-menu-from-python-list-using-flask-and-html
    def index(self):
        form = CancellationForm()
        cancellation = form.del_appointment.data
        slot_delete_option = form.del_openslot.data
        all_slots_delete_option = form.del_all_openslots.data
        if form.validate_on_submit():
            if cancellation:
                appointment_selected = request.form.get('appointment')
                appointment_selected = eval(appointment_selected)
                cancel(appointment_selected, _type="appointment")
            elif slot_delete_option:
                slot_selected = request.form.get('openslot')
                slot_selected = eval(slot_selected)
                cancel(slot_selected, _type='slot')
            elif all_slots_delete_option:
                delete_rows('Slots')
        form.l_appointments = get_from_db(form="list", var="appointments")
        form.l_openslots = get_from_db(form="list", var="slots")
        return self.render('admin/cancellation.html', form=form)

# Create a datastore and instantiate Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
# SQLAlchemyUserDatastore provides helpful methods for identity management tasks e.g. create_user method


security = Security(secureApp, user_datastore)



# This decorator registers a function to be run before the first request to the app
#  i.e. calling localhost:5000 from the browser
# The function does the following things:
# - Create the tables for the users and roles
# - Add a user admin with password admin
# - The user_datastore class will hash the password for us
# - Usubg user_datastore is a better method then db.session.add(Users(email='admin', password='admin') as it shows d
#   to other programmers what is being done and has additional security functions.

# @secureApp.before_first_request
# def create_user():
#     db.drop_all()
#     db.create_all()
#     user_datastore.create_user(email='admin', password='admin')
#     db.session.commit()




########################################################################################################################
# FLASK ADMIN
########################################################################################################################
# Instantiate Flask-Admin
admin = Admin(secureApp, name='Admin', base_template='my_master.html', template_mode='bootstrap3')

########################################################################################################################

# Add the context processor to make variables also accessible to /templates/security/*.html files that extend admin/master.html
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        get_url = url_for,
        h = admin_helpers
    )

# Define the index route
@secureApp.route('/')
@secureApp.route('/index')
def index():
    return render_template('index.html', nav_bar_items=nav_bar_items, page="Home", text=texts_landingpage)


@secureApp.route('/zoekkeuring')
def zoekkeuring():
    return render_template('zoekkeuring.html', nav_bar_items=nav_bar_items, page="Zoek keuring")


@secureApp.route('/mijnverslag')
def mijnverslag():
    return render_template('mijnverslag.html', nav_bar_items=nav_bar_items, page="Uw keuringsverslag")


@secureApp.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', nav_bar_items=nav_bar_items, page="Over ons")


@secureApp.route('/contact')
def contact():
    return render_template('contact.html', nav_bar_items=nav_bar_items, page="Contact")


@app.route('/vragen', methods=['GET', 'POST'])
def vragen():
    search = SearchForm(request.form)
    print(search)
    print(vars(search))
    if request.method == 'POST':
        return search_results(search)
    return render_template('vragen.html', form=search, nav_bar_items=nav_bar_items, page="Vragen")


@app.route('/results')
def search_results(search):
    # request for answer with input question
    search_string = search.data['search']
    QA_SERVER_URL = "http://127.0.0.1:8081"
    r = requests.post(QA_SERVER_URL, json={'question': search_string})
    list_answers = r.content
    list_answers = list_answers.decode('UTF-8')
    null = np.nan
    list_answers = eval(list_answers.encode('unicode_escape'))
    print(list_answers)
    return render_template('search.html', form=search, answers=list_answers, nav_bar_items=nav_bar_items, page="Zoek keuring")


# still have to incorporate selection of time based on location availabilituy
# https://www.youtube.com/watch?v=I2dJuNwlIH0 tutorial
@app.route("/booking", methods=['GET', 'POST'])
def booking():
    form = LocationDateForm()
    l = Slots.query.all()
    form.location.choices = [(i.id, str(i.location)+" | "+ str(i.date.strftime('%d-%m-%Y'))+ " " +str(i.starttime)[0:5]) for i in l]
    if form.validate_on_submit():
        id = form.location.data
        i = Slots.query.filter_by(id=id).first()
        location = str(i.location)+"|"+ str(i.date.strftime('%d-%m-%Y'))+ " " +str(i.starttime)[0:5]
        # datetime = form.datetime.data
        session["appointment"] = location
        session["id"] = i.id
        return redirect(url_for('booking2'))
    return render_template('booking.html', form=form, nav_bar_items=nav_bar_items, page="Afspraak maken")


@app.route("/booking2", methods=['GET', 'POST'])
def booking2():
    form = UserInfoForm()
    last_name = form.last_name.data
    first_name = form.first_name.data
    birthdate = form.birthdate.data
    email = form.email.data
    phone_number = form.phone_number.data
    time=(str(dt.now(timezone.utc).day)+"-"+str(dt.now(timezone.utc).month)+"-"+str(dt.now(timezone.utc).year))
    # validate form on submit and commit to db
    if form.validate_on_submit():
        print("VALIDATED")
        print(session["appointment"])
        choice_appointment = session["appointment"]
        id = session["id"]
        location = choice_appointment.split("|")[0]
        datetime = choice_appointment.split("|")[1]
        create_appointment(location, datetime, first_name, last_name, birthdate, email, phone_number, time, id)
        session['email'] = email
        session['datetime'] = datetime
        # redirect to confirmation page
        return redirect(url_for('confirmation'))
    return render_template('booking2.html', form=form, nav_bar_items=nav_bar_items, page="Afspraak maken")


@app.route("/confirmation", methods=['GET', 'POST'])
def confirmation():
    print(session["appointment"])
    address = session["appointment"].split("|")[0]
    datetime = session["appointment"].split("|")[1]
    worker = "dr. Aaron Schwartz"
    email = session['email']
    data = {"email":email ,"worker":worker,"address":address, "date":datetime}
    payment_link = "paymentlink"
    send_mail(email, payment_link)
    return render_template("confirmation.html", data=data, nav_bar_items=nav_bar_items, page="Afspraak maken")


# Add administrative views to Flask-Admin
admin.add_view(UserModelView(Users, db.session))
admin.add_view(AppointmentsView(Users, db.session, name="Appointments", endpoint='appointments'))
admin.add_view(OpenSlotsView(Users, db.session,name="Open slots", endpoint='slots'))
admin.add_view(ScheduleView(Users, db.session,name="Schedule", endpoint='schedule'))
admin.add_view(CancellationView(Users, db.session,name="Cancellation", endpoint='cancellation'))


if __name__ == '__main__':
    secureApp.run(debug=True)