from app import db, Slots, Appointments, Workers
from datetime import datetime
from datetime import timedelta
import pandas as pd
import os


# MAKE DIFFERENCE BETWEEN PRODUCTION AND DEVELOPMENT ENVIRONMENT
def conn_db():
    if "Users" in os.getcwd():
        from sqlite3 import connect
        con = connect("app.sqlite3")
    else:
        from sqlalchemy import create_engine
        SQL_URI = os.environ.get('DATABASE_URL')
        if SQL_URI and SQL_URI.startswith("postgres://"):
            SQL_URI = SQL_URI.replace("postgres://", "postgresql://", 1)
        con = create_engine(SQL_URI, echo=True)
    return con



def create_slots(location, date, starttime, endtime, timeduration, worker):
    # Create datetime objects for each time (a and b)
    dateTimeA = datetime.combine(date.today(), starttime)
    dateTimeB = datetime.combine(date.today(), endtime)
    # Get the difference between datetimes (as timedelta)
    dateTimeDifference = dateTimeB - dateTimeA
    # max clients in given time: Divide difference in seconds by given timeduration per client in seconds
    number_clients = dateTimeDifference.total_seconds() / (timeduration * 60)
    # loop over max number of clients in given time
    for i in range(abs(int(number_clients))):
        starttime = (dateTimeA + (i * timedelta(minutes=timeduration))).time()
        endtime = (dateTimeA + ((i + 1) * timedelta(minutes=timeduration))).time()
        data = Slots(location, date, starttime, endtime, timeduration, worker)
        db.session.add(data)
    db.session.commit()


def create_appointment(location, datetime, first_name, last_name, birthdate, email, phone_number, time, id):
    # create appointment in appointments table
    data = Appointments(location, datetime, first_name, last_name, birthdate, email, phone_number, time)
    db.session.add(data)
    db.session.commit()
    # remove empty slot from Slots table
    Slots.query.filter_by(id=id).delete()
    db.session.commit()


def get_from_db(form=None, table="appointments"):
    con = conn_db()
    if table == "appointments":
        df = pd.read_sql('SELECT * FROM "Appointments"', con)
    elif table == "slots":
        df = pd.read_sql('SELECT * FROM "Slots"', con)
    elif table == "workers":
        df = pd.read_sql('SELECT * FROM "Workers"', con)
    else:
        df = pd.DataFrame()

    if form == "html":
        if not df.empty:
            df = df.set_index("id")
            df = df.style.set_table_attributes('class="table-primary"')

        return df.to_html(classes=None, index=False)
    elif form == "list":
        return df.values.tolist()
    else:
        return df


def cancel(cancellation, _type):
    con = conn_db()
    cur = con.cursor()
    if _type == 'appointment':
        execution_string= """DELETE FROM "Appointments" WHERE id = '{}';""".format(cancellation[0])
        cur.execute(execution_string)
        con.commit()
        con.close()
        # create_slots(location, date, starttime, endtime, timeduration, worker)
    elif _type == 'slot':
        execution_string= """DELETE FROM "Slots" WHERE id = '{}';""".format(cancellation[0])
        cur.execute(execution_string)
        con.commit()
        con.close()


def delete_rows(table):
    con = conn_db()
    cur = con.cursor()
    if table == 'Appointments':
        execution_string= """DELETE FROM "Appointments";"""
        cur.execute(execution_string)
        con.commit()
        con.close()
    if table == 'Slots':
        execution_string= """DELETE FROM "Slots";"""
        cur.execute(execution_string)
        con.commit()
        con.close()


def get_ninja_tables():
    html_table_slots = get_from_db(form='html', table='slots')
    html_table_appointments = get_from_db(form='html', table='appointments')
    html_table_workers = get_from_db(form='html', table='workers')
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
    return tables_ninja


# CRUD doctors -> do later, not necessary now
if __name__ == '__main__':
    from datetime import datetime as dt
    from datetime import timedelta
    from app import db, Slots
    date = dt.now()
    data = Slots("Rdam", date, dt.now().time(), (dt.now() + timedelta(minutes=60)).time(), 10, "ASDSA")
    db.session.add(data)
    db.session.commit()
    create_slots("Rdam", date, dt.now().time(), (dt.now() + timedelta(minutes=60)).time(), 10, "ASDSA")