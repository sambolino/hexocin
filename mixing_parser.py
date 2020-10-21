import sys
import argparse
from calculate_and_plot import *

def _n_range(val):
    ival = int(val)
    if val not in range (4, 20):
        raise argparse.ArgumentTypeError("n value should be between 4 and 20")

def _p_range(val):
    ival = int(val)
    if val not in range (1, 5):
        raise argparse.ArgumentTypeError("p value should be between 1 and 5")

def _t_range(val):
    ival = int(val)
    if val not in range (1, 50000):
        raise argparse.ArgumentTypeError("t value should be between 1 and 50000")

PARSER = argparse.ArgumentParser(description="", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

PARSER.add_argument("-n", type=_n_range, default=None, help="aaa", required=True)
PARSER.add_argument("-p", type=_p_range, default=None, help="aaa", required=True)
PARSER.add_argument("-t", type=_t_range, default=None, help="aaa", required=True)
ARGS = PARSER.parse_args()

if __name__ == "__main__":
    sys.exit(calculate_and_plot(ARGS.n, ARGS.p, ARGS.t))
