from sqlite_utils import *
import math
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def calculate_and_plot(n, p, temperature):

    database = r"data/mixing_agn.db"
    conn = create_connection(database)

    with conn:
        row = select_row(conn, n, p)

    x1 = temperature
    x = np.array([2000, 3000, 5000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000])
    y = np.array([float(s) for s in row.split(",")])
    f = interp1d(x, y, fill_value="extrapolate")
    f2 = interp1d(x, y, kind='cubic', fill_value="extrapolate")

    
    xnew = np.linspace(2000, 30000, num=41, endpoint=True)
    xinter1 = np.linspace(0, 1999, num=5, endpoint=True)
    xinter2 = np.linspace(30001, 50000, num=30, endpoint=True)
    x0 = 15

    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
    
    plt.plot(x, y, 'bo', markersize=4)
    plt.plot(x1, f2(x1), 'gx', markersize=11)
    #plt.plot(xnew, f(xnew), '-')
    plt.plot(xnew, f2(xnew), '--', color="purple")
    plt.plot(xinter1, f2(xinter1), '--', color="thistle")
    plt.plot(xinter2, f2(xinter2), '--', color="thistle")
    plt.legend(['data points', 'your point: [%d, %f]' % (x1,f2(x1)), 'cubic interpolation', 'extrapolation'], loc='best')
    plt.title('Excitation rate coefficients (n=%d, n\'=%d)' % (n, n+p), fontdict=font)
    plt.xlabel('temperature (K)', fontdict=font)
    plt.ylabel(r'$K_{n;n + p}(T)$ ($10^{-9} {cm}^{3}\,\,{s}^{-1}$)', fontdict=font)

    plt.show()
