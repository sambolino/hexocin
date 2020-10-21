import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql = """ CREATE TABLE IF NOT EXISTS data_points (
                                    n integer NOT NULL,
                                    p integer NOT NULL,
                                    data text NOT NULL
                                ); """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def populate_table(conn, row):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO data_points(n,p,data)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()
    return cur.lastrowid

def select_row(conn, n, p):
    """
    Return single row from data_points table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT data FROM data_points where n=%d and p=%d" % (n, p))

    return cur.fetchone()[0]
