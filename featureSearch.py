import kFold
import copy
def featureSearch(myData):
    setOfFeatures = []
    bestSet = []
    bestSoFar = 0

    for i in range(1, len(myData[0])):#for each val in a row
        print('on the ' + str(i) +'th level of the search tree')
        featureToAdd = 0
        localBest = 0
        for k in range(1, len(myData[0])):#for each val in a row
            if k not in setOfFeatures:
                print('--considering adding the ' + str(k) + 'th feature')
                accuracy = kFold.leaveOneOut(myData, setOfFeatures, k)
                if(accuracy > localBest):
                    localBest = accuracy
                    featureToAdd = copy.deepcopy(k)
        if(localBest > bestSoFar):
            bestSet.append(copy.deepcopy(featureToAdd))
            bestSoFar = localBest
        setOfFeatures.append(featureToAdd)
        print('--on the ' + str(i) +'th level, added feature ' + str(featureToAdd))
        
    toRet = []
    toRet.append(bestSoFar)
    toRet.append(bestSet)
    return toRet