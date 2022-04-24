from flask_admin import Admin, expose
from flask_admin import helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, Security, SQLAlchemyUserDatastore
from flask import render_template, url_for,  redirect
from forms import LocationDateForm, ScheduleForm, CancellationForm, SearchForm
from flask import request, session
from helpers.mail import send_mail
import os
from helpers.file_encryptor import Encryptor
from app import secureApp, db, Users, Roles, Slots, app
from datetime import datetime as dt
from datetime import timezone
from planningOS import create_slots, create_appointment, get_ninja_tables, get_from_db, cancel, delete_rows, send_backup
import requests
import numpy as np
from definitions import nav_bar_items, landingpage_items, dict_payments_links, list_services, address_list
from texts import texts_landingpage, welcome_message_whatsapp, \
    texts_inloopspreekuur, texts_mijnkeuring, texts_aboutus, \
    texts_contact, texts_inhoudkeuring
from dateutil.parser import parse
import threading as thr
from dotenv import load_dotenv

load_dotenv()


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
        html_table_slots = get_from_db(form='html', table='openslots')
        html_table_appointments = get_from_db(form='html',table='appointments')
        html_table_workers = get_from_db(form='html',table='workers')
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
        BIG = form.BIG.data
        if form.validate_on_submit():
            create_slots(location, date, starttime, endtime, timeduration, worker, BIG)
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
        form.l_appointments = get_from_db(form="list", table="appointments")
        form.l_openslots = get_from_db(form="list", table="slots")
        return self.render('admin/cancellation.html', form=form)

# Create a datastore and instantiate Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
# SQLAlchemyUserDatastore provides helpful methods for identity management tasks e.g. create_user method


security = Security(secureApp, user_datastore)


# This decorator registers a function to be run before the first request to the app
#  i.e. calling localhost:5000 from the browser
# The function does the following things:
# - Create the tables for the users and roles
# - Add a user with an email  and with passworddefined in .env file admin
# - The user_datastore class will hash the password for us
# - Usubg user_datastore is a better method then db.session.add(Users(email='admin', password='admin') as it shows d
#   to other programmers what is being done and has additional security functions.
# DO NOT USE ADMIN AS PASSWORD!!!!

@secureApp.before_first_request
def create_user():
    if os.environ.get("FLASK_ENV") == "development":
        db.drop_all()
        db.create_all()
        email = os.environ.get('admin_email')
        password = os.environ.get('admin_password')
        user_datastore.create_user(email=email, password=password)
        db.session.commit()
        import pandas as pd
        df = pd.read_pickle("test_slots.pkl")
        if "Users" in os.getcwd():
            from sqlite3 import connect
            con = connect("app.sqlite3")
        else:
            from sqlalchemy import create_engine
            SQL_URI = os.environ.get('DATABASE_URL')
            if SQL_URI and SQL_URI.startswith("postgres://"):
                SQL_URI = SQL_URI.replace("postgres://", "postgresql://", 1)
            con = create_engine(SQL_URI, echo=True)
        df.to_sql("Slots", con=con, if_exists='append', index=False)



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
    global welcome_message_whatsapp
    return render_template('index.html', nav_bar_items=nav_bar_items, page="Home",
                           text=texts_landingpage, landingpage_items=landingpage_items,
                           welcome_message=welcome_message_whatsapp)


@secureApp.route('/inloopspreekuur')
def inloopspreekuur():
    return render_template('inloopspreekuur.html', nav_bar_items=nav_bar_items, page="Inloopspreekuur", text=texts_inloopspreekuur)


@secureApp.route('/zoekkeuring')
def zoekkeuring():
    return render_template('zoekkeuring.html', nav_bar_items=nav_bar_items, page="Zoek keuring")


@secureApp.route('/mijnverslag')
def mijnverslag():
    return render_template('mijnverslag.html', nav_bar_items=nav_bar_items, page="Uw keuringsverslag", text=texts_mijnkeuring)


@secureApp.route('/inhoudkeuring')
def inhoudkeuring():
    return render_template('inhoudkeuring.html', nav_bar_items=nav_bar_items, page="Inhoud keuring", text=texts_inhoudkeuring)

@secureApp.route('/prijzen')
def prijzen():
    return render_template('prijzen.html', nav_bar_items=nav_bar_items, page="Prijzen", text=list_services)


@secureApp.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', nav_bar_items=nav_bar_items, page="Over ons", text=texts_aboutus)


@secureApp.route('/contact')
def contact():
    return render_template('contact.html', nav_bar_items=nav_bar_items, page="Contact", text=texts_contact, welcome_message=welcome_message_whatsapp)


@app.route('/vragen', methods=['GET', 'POST'])
def vragen():
    search = SearchForm(request.form)
    # print(search)
    # print(vars(search))
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
    list_answers = eval(list_answers.encode('unicode_escape'))
    # print(list_answers)
    return render_template('search.html', form=search, answers=list_answers, nav_bar_items=nav_bar_items, page="Zoek keuring")


# still have to incorporate selection of time based on location availabilituy
# https://www.youtube.com/watch?v=I2dJuNwlIH0 tutorial
@app.route("/booking", methods=['GET', 'POST'])
def booking():
    form = LocationDateForm()
    l = get_from_db(table="slots", form="earliest-time-slots-list")
    form.location.choices = [
        (i[0], str(i[1].split(",")[-1]).strip() + " | " + str(parse(str(i[2])).strftime('%d-%m-%Y')) + " " + str(i[3].time())[0:5])
        for i in l]

    last_name = form.last_name.data
    first_name = form.first_name.data
    birthdate = form.birthdate.data
    email = form.email.data
    phone_number = form.phone_number.data
    time=(str(dt.now(timezone.utc).day)+"-"+str(dt.now(timezone.utc).month)+"-"+str(dt.now(timezone.utc).year))
    print("loading")
    if form.validate_on_submit():

        print("submitted")
        id = form.location.data
        i = Slots.query.filter_by(id=id).first()
        session["id"] = i.id
        session["worker"] = i.worker
        session["BIG"] = i.BIG
        location = str(i.location)+"|" + str(i.date.strftime('%d-%m-%Y')) + " " + str(i.starttime)[0:5]
        session["appointment"] = location
        session["type_service"] = form.type_service.data
        # print(form.type_service.data)
        # print(session["appointment"])
        choice_appointment = session["appointment"]
        id = session["id"]
        location = choice_appointment.split("|")[0]
        datetime = choice_appointment.split("|")[1]
        create_appointment(location, datetime, first_name, last_name, birthdate, email, phone_number, time, id)
        session['email'] = email
        session['datetime'] = datetime
        print(session)
        # redirect to confirmation page
        return redirect(url_for('confirmation'))
    return render_template('booking.html', form=form, nav_bar_items=nav_bar_items, address_list=address_list, page="Afspraak maken")


@app.route("/confirmation", methods=['GET', 'POST'])
def confirmation():
    print(session["appointment"])
    print("confirmation function")
    address = session["appointment"].split("|")[0]
    datetime_appointment = session["appointment"].split("|")[1]
    type_service = session["type_service"]
    worker = session["worker"]
    email = session['email']
    BIG = session["BIG"]
    payment_link = dict_payments_links[type_service]
    type_service = dict(list_services).get(type_service)
    data = {"email":email ,"worker":worker,"address":address, "date":datetime_appointment, "type_service": type_service,
            "payment_link":payment_link, "BIG":BIG} # added extra data to form for future corrections if necessary
    send_mail(email, datetime_appointment=datetime_appointment, type_service=type_service.split("€")[0][:-1],address=address,
              worker=worker, BIG=BIG, payment_link=payment_link,attachment=None)
                # remove euro sign in type service to prevent errors
    send_mail(os.environ.get("DEVELOPER"), subject="Nieuwe klant")
    df = get_from_db()
    df.to_csv("backup.csv")
    fe = Encryptor()
    key = fe.key_load()
    fe.file_encrypt(key, "backup.csv", "backup.csv")
    thr.Thread(target=send_backup).start()
    return render_template("confirmation.html", data=data, nav_bar_items=nav_bar_items, page="Afspraak maken")


# Add administrative views to Flask-Admin
admin.add_view(UserModelView(Users, db.session))
admin.add_view(AppointmentsView(Users, db.session, name="Appointments", endpoint='appointments'))
admin.add_view(OpenSlotsView(Users, db.session,name="Open slots", endpoint='slots'))
admin.add_view(ScheduleView(Users, db.session,name="Schedule", endpoint='schedule'))
admin.add_view(CancellationView(Users, db.session,name="Cancellation", endpoint='cancellation'))


if __name__ == '__main__':
    if os.environ.get("FLASK_ENV") == "development":
        secureApp.run(host='0.0.0.0', port=8080, debug=True)
    else:
        secureApp.run(debug=False)