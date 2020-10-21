from sqlite_utils import *
import math
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def calculate_and_plot(n, nprim, temperature):

    database = r"data/mixing_agn.db"
    conn = create_connection(database)

    with conn:
        row = select_row(conn, n, nprim)

    x = np.array([2000., 3000,    5000,   7000,    8000,    9000,    10000,   15000,   20000,   25000,   30000])
    y = np.array([float(s) for s in row.split(",")])
    f = interp1d(x, y, fill_value="extrapolate")
    f2 = interp1d(x, y, kind='cubic', fill_value="extrapolate")

    xnew = np.linspace(0, 50000, num=41, endpoint=True)
    plt.plot(x, y, 'bo', markersize=4)
    plt.plot(x1, f2(x1), 'gx', markersize=11)
    #plt.plot(xnew, f(xnew), '-')
    plt.plot(xnew, f2(xnew), '--', color="orange")
    plt.legend(['data points', 'your point: %s, %s' % (x1,f2(x1)), 'cubic interpolation'], loc='best')
    plt.show()
