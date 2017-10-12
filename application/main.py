from flask import Flask, render_template, flash, redirect
# from app import app
from forms import UserForm
import logging
import psycopg2
logging.basicConfig(level=logging.DEBUG)
logging.warning('Watch out!')

app = Flask(__name__)
app.secret_key = "mysecret"
logging.info("pre try")

DB_USER = 'test'
DB_PASS = 'test'
DB_NAME = 'test_db'
DB_HOST = 'postgresql'
# DB_PORT = '5432'

conn = psycopg2.connect("dbname='{0}' user='{1}' password='{2}' host='{3}'".format(DB_NAME, DB_USER, DB_PASS, DB_HOST))
cur = conn.cursor()

def create_table(tablename):
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS {0}(ID INT PRIMARY KEY NOT NULL)".format(tablename))
    except psycopg2.OperationalError as e:
        logging.error('Unable to connect!\n{0}').format(e)
        pass

@app.route('/<string:tablename>/add', methods=['GET','POST'])
def add_user(tablename):
    create_table(tablename)
    form = UserForm()
    if form.validate_on_submit:
        flash('Login requested for OpenID="%s"' % (form.userid.data))
        try:
            cur.execute("INSERT INTO {0} VALUES {1}".format(tablename, form.userid.data))
            return redirect('/tables')
        except:
            logging.error('Unable to insert data into {0}'.format(tablename))
    return render_template('user.html', title='Add User', form=form)

@app.route('/<string:tablename>/request', methods=['GET'])
def retrieve_user(tablename):
    create_table(tablename)
    try:
        cur.execute("SELECT * FROM {0}".format(tablename))
        return "Data retrieved from {0}".format(tablename)
    except pyscopg2.OperationalError as e:
        logging.error('Unable to retreive data from {0}'.format(tablename))
        pass

@app.route("/<string:tablename>")
def hello_world(tablename):
    create_table(tablename)
    return "Created table: {0}".format(tablename)

# @app.route("/<string:tablename>/request", methods = ['GET','POST'])
# def user_data(tablename):
#     create_table(tablename)
#     if request.method == 'GET':
#         try:
#             cur.execute("SELECT * FROM {0}".format(tablename))
#             return "Data retrieved from {0}".format(tablename)
#         except pyscopg2.OperationalError as e:
#             logging.error('Unable to retreive data from {0}'.format(tablename))
#             pass
#     if request.method == 'POST':
#         try:
#             cur.execute("INSERT INTO {0} VALUES (3);".format(tablename))
#             return "Inserted data into {0}".format(tablename)
#         except pyscopg2.OperationalError as e:
#             logging.error('Unable to insert data into {0}'.format(tablename))
#             pass


@app.route("/tables")
def tables_print():
    try:
        cur.execute("SELECT * FROM pg_catalog.pg_tables");
    except psycopg2.OperationalError as e:
        logging.error('Unable to connect!\n{0}').format(e)
        pass
    res = ""
    for record in cur:
        res = res + ", " + str(record)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
