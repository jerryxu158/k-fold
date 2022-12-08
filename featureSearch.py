import kFold
import copy
def featureSearch(myData):
    setOfFeatures = []
    bestSet = []
    bestSoFar = 0

    for i in range(1, len(myData[0])):#for each val in a row
        #print('on the ' + str(i) +'th level of the search tree')
        featureToAdd = 0
        localBest = 0
        for k in range(1, len(myData[0])):#for each val in a row
            if k not in setOfFeatures:
                #print('--considering adding the ' + str(k) + 'th feature')
                accuracy = kFold.leaveOneOut(myData, setOfFeatures, k)
                if(accuracy > localBest):
                    localBest = accuracy
                    featureToAdd = copy.deepcopy(k)
        if(localBest > bestSoFar):
            bestSet.append(copy.deepcopy(featureToAdd))
            bestSoFar = localBest
        setOfFeatures.append(featureToAdd)
        print('\n--on level ' + str(i) +', added feature ' + str(featureToAdd))
        print('current set of features is: ', end='')
        print(setOfFeatures)
        print('This set\'s accuracy was ' + str(localBest))
        print('')
        
    toRet = []
    toRet.append(bestSoFar)
    toRet.append(bestSet)
    return toRet

def backwardElim(myData):
    setOfFeatures = []
    bestSet = []
    bestSoFar = 0
    featureToRemove = -1
    for i in range(1, len(myData[0])):
        setOfFeatures.append(i)
    for i in range(0,len(myData[0]) - 1):
        bestInLevel = 0
        if(i == 0):
            accuracy = kFold.backwardsLeaveOneOut(myData, setOfFeatures, 0)
            print('\n--on level ' + str(i) +', removed feature ' + str(featureToRemove))
            print('set of features is currently:')
            print(setOfFeatures)
            print('')
            print('this sets accuracy was: ' + str(accuracy))
        else:
            for j in setOfFeatures:
                accuracy = kFold.backwardsLeaveOneOut(myData, setOfFeatures, j)
                if accuracy > bestInLevel:
                    featureToRemove = j
                    bestInLevel = accuracy
            setOfFeatures.remove(featureToRemove)
            if(bestInLevel > bestSoFar):
                bestSet = copy.deepcopy(setOfFeatures)
                bestSoFar = bestInLevel
            print('\n--on level ' + str(i) +', removed feature ' + str(featureToRemove))
            print('set of features is currently:')
            print(setOfFeatures)
            print('')
            print('this sets accuracy was: ' + str(bestSoFar))
    toRet=[]
    toRet.append(bestSoFar)
    toRet.append(bestSet)
    return toRet
        
        
