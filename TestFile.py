import sys
import random

# read and write files using built-in Python methods
def main():
    # redirect output to file
    sys.stdout = open("test.txt", "w")
    # create 1000 data points for testing purposes
    for i in range(1000):
        print([random.uniform(0.8,1.2) for _ in range(5)])
main()