import re
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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def populate_table(conn, row):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO data_points(d,p,data)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()
    return cur.lastrowid

def chunks(l, n):
    """ split list l to chunks based on size of chunk n """
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def main():
    f = open("Supporting_info.txt")

    all_lines = f.readlines()
    selected_lines = []

    for line in all_lines:
        if line.startswith('n=') or re.match(r'^[1-5] ', line):
            selected_lines.append(line)

    #remove \n's
    selected_lines = [line.rstrip() for line in selected_lines]

    chk = chunks(selected_lines, 6)

    list_of_dicts = []
    for line in chk:
        for i in range(5):
            dic = {"n":re.sub("[^0-9]", "", line[0]), 
                    "p":line[i+1][:1],
                    "data":[float(s) for s in line[i+1][2:].split(" ")]}
            list_of_dicts.append(dic)

    #print(list_of_dicts)
    database = r"mixing_agn.db"
    conn = create_connection(database)

    sql_create_table = """ CREATE TABLE IF NOT EXISTS data_points (
                                        d integer NOT NULL,
                                        p integer NOT NULL,
                                        data text NOT NULL
                                    ); """

    if conn is not None:
        create_table(conn, sql_create_table)

    with conn:
        for dic in list_of_dicts:
            #print(dic)
            populate_table(conn, (dic['n'], dic['p'], ','.join(map(str, dic['data']))))

if __name__ == '__main__':
    main()
