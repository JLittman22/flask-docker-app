from flask import Flask
import logging

import psycopg2
logging.basicConfig(level=logging.DEBUG)
logging.warning('Watch out!')

app = Flask(__name__)
logging.info("pre try")

DB_USER = 'test'
DB_PASS = 'test'
DB_NAME = 'test_db'
DB_HOST = 'postgresql'
# DB_PORT = '5432'

conn = psycopg2.connect("dbname='{0}' user='{1}' password='{2}' host='{3}'".format(DB_NAME, DB_USER, DB_PASS, DB_HOST))
cur = conn.cursor()

@app.route("/<string:tablename>")
def hello_world(tablename):
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS {0}(ID INT PRIMARY KEY NOT NULL)".format(tablename));
    except psycopg2.OperationalError as e:
        logging.error('Unable to connect!\n{0}').format(e)
        pass
    return "Created table: {0}".format(tablename)

@app.route("/tables")
def tables_print():
    cur.execute("SELECT * FROM pg_catalog.pg_tables");
    res = ""
    for record in cur:
        res = res + ", " + str(record)
    return res

@app.route("/path", endpoint='func2')
def func2():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
