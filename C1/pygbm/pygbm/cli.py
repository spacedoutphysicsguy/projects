import argparse
from .gbm import GBM
import os
import numpy as np


def main():
    parser= argparse.ArgumentParser("gbm",description="simulate brownian motion")
    parser.add_argument("--Y0",type=float,required=True,help="initial price")
    parser.add_argument("--mu",type=float,required=True,help="drift coefficient")
    parser.add_argument("--sigma",type=float,required=True,help="volatility")
    parser.add_argument("--T",type=float,default=2.0,help="time period")
    parser.add_argument("--N",type= int,default=100,help="Number of steps")

    args= parser.parse_args()
    gbmpath= np.column_stack(GBM(args.Y0,args.mu,args.sigma).simulate_path(args.T,args.N))
    filepath= os.path.join(os.getcwd(),"gbmsim.txt")
    np.savetxt(filepath,gbmpath,delimiter=",",header="t,Y_t")


if __name__== "__main__":
    main()

