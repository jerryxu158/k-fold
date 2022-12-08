import parseCSV
import featureSearch
import time

rows = parseCSV.parse()
print('would you like to do forward search(1) or backwards elimination(2)?')
ans = input()

start = time.time()
if(ans == '1'):
    res = featureSearch.featureSearch(rows)
elif(ans == '2'):
    res = featureSearch.backwardElim(rows)
else:
    print('unknown input, exiting')
    exit()
timeSpent = str(time.time()-start)
timeSpent = timeSpent[0:(timeSpent.find('.')+3)]
print('time spent was approximately: ' + timeSpent)
print('best accuracy was: ' + str(res[0]))
print('set of features was: ' + str(res[1]))