# Task 12

# - Pass two command line arguments (numbers) and add them together.

# - Run tests in your repo automatically using GitHub Actions.

# References:
# argparse

import argparse

def multiply(a,b):
        return a * b
    
def add(a,b):
    return a + b

def arithematic():
    # creating parser object
    parser = argparse.ArgumentParser(prog="arithematic",
                                     description="pass intergers for addition and multiplication through command line",
                                     epilog="program to learn how to pass arguments through command line")

    # add arguments for adding
    parser.add_argument('arg1',metavar="a", type=int, help='first number')
    parser.add_argument('arg2',metavar="b", type=int, help='second number')
    parser.add_argument("-m","--multiply",dest="operation",default=add,action="store_const",const=multiply,help="specify the operation o")
    args = parser.parse_args()

    if args.operation is add :
         print(f"{args.arg1} + {args.arg2} = {args.arg1 + args.arg2}")
    else:
         print(f"{args.arg1} x {args.arg2} = {args.arg1 * args.arg2}") 
    
if __name__ == "__main__":
    arithematic()