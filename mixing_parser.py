import sys
import argparse
from calculate_and_plot import *

def _n_range(val):
    if int(val) not in range (4, 21):
        raise argparse.ArgumentTypeError("n value should be between 4 and 20")
    return int(val)

def _p_range(val):
    if int(val) not in range (1, 6):
        raise argparse.ArgumentTypeError("p value should be between 1 and 5")
    return int(val)

def _t_range(val):
    if int(val) not in range (1, 50001):
        raise argparse.ArgumentTypeError("t value should be between 1 and 50000")
    return int(val)

PARSER = argparse.ArgumentParser(description="", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

PARSER.add_argument("-n", "--n", type=_n_range, default=None, help="Quantum number (between 4 and 20)", required=True)
PARSER.add_argument("-p", "--p", type=_p_range, default=None, help="Transition from n to n' (between 1 and 5)", required=True)
PARSER.add_argument("-t", "--temp", type=_t_range, default=None, help="Temperature (between 2000 and 50000)", required=True)
ARGS = PARSER.parse_args()

if __name__ == "__main__":
    sys.exit(calculate_and_plot(ARGS.n, ARGS.p, ARGS.temp))
