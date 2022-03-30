from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from planningOS import get_from_db
from definitions import list_services

class SearchForm(FlaskForm):
    search = StringField('')
    type = "search"


class UserInfoForm(FlaskForm):
    last_name = StringField('Achternaam', validators=[InputRequired(message="Vul naam in "), Length(min=2, max=30)])
    first_name = StringField('Voornaam', validators=[DataRequired(), Length(min=2, max=30)])
    birthdate = DateField('Geboorte datum', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Telefoonnummer', validators=[DataRequired(), Length(min=10, max=14)])
    submit = SubmitField('Maak een afspraak')


class LocationDateForm(FlaskForm):
    # READ OPEN SLOTS FROM OPEN SLOTS DB
    # EXTRACT LOCATION AND DATETIMES OF OPEN SLOTS AND CONVERT TO LISTS
    location = SelectField("", validators=[DataRequired()])
    type_service = SelectField("", choices=list_services, validators=[DataRequired()])
    # datetime = SelectField("Selecteer dag en tijd", validators=[DataRequired()],choices=["Maandag 3 november","Dinsdag 4 november"])
    submit = SubmitField('Volgende')


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
