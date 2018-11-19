########################################################################################################################
# SCA Algorithm: RRMean with Plots                                                                                     #
# Author: Mark Maroki                                                                                                  #
#                                                                                                                      #
# This program simulates data taken per second from the Apple Watch 4 ECG and calculates the average.                  #
# In addition, this program uses matplotlib to plot the results on both a scatter plot and a histogram.                #
#                                                                                                                      #
########################################################################################################################

# generate related variables
import matplotlib.pyplot as plt


def main():
    # use the test data to gather results
    with open ("test.txt", "r") as testFile:
        # count can be used to simulate time
        count = 0
        avgList = []
        for line in testFile:
            # increment count by 1 (for real data, this will be in seconds)
            count = count + 1

            #prepare data
            x = count   # implemented to simulate time
            y = rrmean(line) #average of all of the data
            # place values into a list
            avgList.append(y)

            #instantiate figure/plot 1 (scatter plot)
            plt.figure(1)
            plt.scatter(x,y)
        # add title and show the plotted data points
        plt.suptitle("Random Data Averages")

        # reverse list so it can go in proper order
        avgList.reverse()

        # instantiate figure 2 (histogram)
        plt.figure(2)

        # plot histogram
        plt.hist(avgList, 250)

        # display plot results
        plt.show()

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

#close main
main()