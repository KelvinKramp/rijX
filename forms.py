from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from planningOS import get_from_db
from definitions import list_services

class SearchForm(FlaskForm):
    search = StringField('')
    type = "search"


class LocationDateForm(FlaskForm):
    last_name = StringField('Achternaam', name="Achternaam",validators=[InputRequired(message="Vul naam in "), Length(min=2, max=30)])
    first_name = StringField('Voornaam', name="Voornaam", validators=[DataRequired(), Length(min=2, max=30)])
    birthdate = DateField('Geboorte datum', name="Geboortedatum", validators=[DataRequired()])
    email = StringField('Email', name="Email",validators=[DataRequired(), Email()])
    phone_number = StringField('Telefoonnummer', name="Telefoonnummer",validators=[DataRequired(), Length(min=10, max=14)])
    submit = SubmitField('Maak een afspraak')
    location = SelectField("Lokatie en datum", name="Lokatie en datum",validators=[DataRequired()])
    type_service = SelectField("Type keuring", name="Type keuring",choices=list_services, validators=[DataRequired()])
    # datetime = SelectField("Selecteer dag en tijd", validators=[DataRequired()],choices=["Maandag 3 november","Dinsdag 4 november"])
    submit = SubmitField('Bevestigen')


class CancellationForm(FlaskForm):
    l_appointments = get_from_db(form="list",table="appointments")
    l_openslots = get_from_db(form="list",table="openslots")
    del_appointment = SubmitField('Delete appointment')
    del_openslot = SubmitField('Delete open slot')
    del_all_openslots = SubmitField('Delete all open slot')


class ScheduleForm(FlaskForm):
    # READ OPEN SLOTS FROM OPEN SLOTS DB
    # EXTRACT LOCATION AND DATETIMES OF OPEN SLOTS AND CONVERT TO LISTS
    location = SelectField("Selecteer locatie", validators=[DataRequired()],choices=["Rotterdam Noord", "Rotterdam Zuid"])
    date = DateField('Datum', validators=[DataRequired()]) # format='%Y-%m-%d %H:%M:%S
    starttime = TimeField('Starttijd', validators=[DataRequired()]) # format='%Y-%m-%d %H:%M:%S
    endtime = TimeField("Eindtijd", validators=[DataRequired()])
    timeduration =  SelectField("Selecteer ", validators=[DataRequired()],choices=["10 min", "15 min", "20 min", "25 min", "30 min"])
    worker = StringField('Naam', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Submit')
