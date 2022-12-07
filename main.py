import parseCSV
import featureSearch
import time

rows = parseCSV.parse()

start = time.time()
res = featureSearch.featureSearch(rows)
print('time spent was aproximately: ' + str(time.time()-start))
print('best accuracy was: ' + str(res[0]))
print('set of features was: ' + str(res[1]))