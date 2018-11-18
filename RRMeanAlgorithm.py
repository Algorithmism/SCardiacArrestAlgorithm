# generate related variables

from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot

# seed random number generator
#seed(1)

# prepare data
#x = 20 * randn(1000) + 100
# y = x + (10 * randn(1000) + 50)
# # summarize
# print('x: mean=%.3f stdv=%.3f' % (mean(x), std(x)))
# print('y: mean=%.3f stdv=%.3f' % (mean(y), std(y)))
# # plot
# pyplot.scatter(x, y)
# pyplot.show()

def main():
    a = [1,2,3]
    print(rrmean(a,12,40))

def rrmean(vals, N, time):

    #param N is how many entries/data points
    n = len(vals)

    #start sum at init 0
    totalSum = 0

    #sum up the data point values
    for i in range(n):
        totalSum += vals[i]
        i = i+1
    totalSum = sum(vals)

    #total sum divided by the length of the list of numbers
    avg = totalSum/n
    #return the average
    return (avg)

main()