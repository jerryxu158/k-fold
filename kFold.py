import random
import copy
import math
def leaveOneOut(myData, setOfFeatures, featureToAdd):
    numCorrect = 0
    currSet = copy.deepcopy(setOfFeatures)
    currSet.append(featureToAdd)
    #print('     checking to see accuracy of: ')
    #print('         ', end='')
    #print(currSet)
    for i in range(len(myData)):
        objectToClasify = myData[i]
        label = myData[i][0]

        nearestDistance = 10000000
        nearestLocation = 10000000
        nearestLabel = -1

        for k in range (1,len(myData)):
            if k != i:
                distance = 0.0
                tempDist = 0.0
                for j in currSet:
                    tempDist += pow((objectToClasify[j] - myData[k][j]),2)
                distance += math.sqrt(tempDist)
                if distance < nearestDistance:
                    nearestDistance = distance
                    nearestLocation = k
                    nearestLabel = myData[nearestLocation][0]
        if(label == nearestLabel):
            numCorrect += 1
    #print('         accuracy was ' + str(numCorrect/ len(myData[1:])))
    return numCorrect/ len(myData[1:])

def backwardsLeaveOneOut(myData, setOfFeatures, featureToAdd = 0):
    numCorrect = 0
    currSet = copy.deepcopy(setOfFeatures)
    if featureToAdd != 0:
        currSet.remove(featureToAdd)
    #print('     checking to see accuracy of: ')
    #print('         ', end='')
    #print(currSet)
    for i in range(len(myData)):
        objectToClasify = myData[i]
        label = myData[i][0]

        nearestDistance = 10000000
        nearestLocation = 10000000
        nearestLabel = -1

        for k in range (1,len(myData)):
            if k != i:
                distance = 0.0
                tempDist = 0.0
                for j in currSet:
                    tempDist += pow((objectToClasify[j] - myData[k][j]),2)
                distance = math.sqrt(tempDist)
                if distance < nearestDistance:
                    nearestDistance = distance
                    nearestLocation = k
                    nearestLabel = myData[nearestLocation][0]
        if(label == nearestLabel):
            numCorrect += 1
    #print('         accuracy was ' + str(numCorrect/ len(myData[1:])))
    return numCorrect/ len(myData[1:])