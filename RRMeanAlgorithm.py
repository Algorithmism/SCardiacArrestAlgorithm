# generate related variables
import sys
from numpy import mean
from numpy import std
from numpy.random import randn

from matplotlib import pyplot

def main():
    with open ("test.txt", "r") as testFile:
        count = 0
        for line in testFile:
            count = count + 1
            print(rrmean(line))
            #prepare data
            x = count
            y = rrmean(line)
            #plot
            pyplot.scatter(x,y)
        pyplot.suptitle("Random Data Averages")
        pyplot.show()


# rrmean algorithm cal
def rrmean(line):

    # remove end brackets (strings are immutable)
    line = line.replace('[','')
    line = line.replace(']', '')

    # create list of strings separated by comma
    valListCopy = line.split(',')

    # Convert string elements to double
    valList = [float(i) for i in valListCopy]
    # param N is how many entries/data points
    n = len(valList)

    # start sum at init 0
    totalSum = 0

    # sum up the data point values in the list of floats
    for i in range(n):
        totalSum += valList[i]
        i = i+1
    # get the sum needed for the average variable below
    totalSum = sum(valList)

    # total sum divided by the length of the list of numbers
    avg = totalSum/n

    # return the average
    return (avg)

main()