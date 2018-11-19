########################################################################################################################
# SCA Algorithm: RRMean with Plot                                                                                      #                   #                                                                                      #
# Author: Mark Maroki                                                                                                  #
#                                                                                                                      #
# This program calculates the average of a list of data and uses matplotlib to plot these averages.                    #
# This program simulates data taken from the Apple Watch 4 ECG per second and calculates the average.                  #
########################################################################################################################

# generate related variables

from matplotlib import pyplot

def main():
    #use the test data to gather results
    with open ("test.txt", "r") as testFile:
        #count can be used to simulate time
        count = 0

        for line in testFile:
            #increment count by 1 (for real data, this will be in seconds)
            count = count + 1

            #prepare data
            x = count   #implemented to simulate time
            y = rrmean(line) #average of all of the data

            #plot
            pyplot.scatter(x,y)
        #add title and show the plotted data points
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