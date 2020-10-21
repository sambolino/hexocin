import re
import sqlite3
from sqlite3 import Error
from sqlite_utils import *

def chunks(l, n):
    """ split list l to chunks based on size of chunk n """
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def main():
    f = open("data/Supporting_info.txt")

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
    database = r"data/mixing_agn.db"
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)

    with conn:
        for dic in list_of_dicts:
            populate_table(conn, (dic['n'], dic['p'], ','.join(map(str, dic['data']))))

if __name__ == '__main__':
    main()
