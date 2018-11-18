import sys
import random

# read and write files using built-in Python methods
def main():
    # redirect output to file
    sys.stdout = open("test.txt", "w")
    # create 1000 data points for testing purposes
    for i in range(1000):
        print([random.random() for _ in range(5)])
main()