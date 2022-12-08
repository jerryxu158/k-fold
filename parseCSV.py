import copy
def parse():
    rows = []
    with open('D:\school stuff\classes\cs 170\projects\project 2\CS170_Large_Data__31.txt') as f:
        lines = f.readlines()
        for i in lines:
            line = i.strip('\n').split('  ')
            try:
                line.remove('')
            except:
                continue
            for j in range(len(line)):
                if line[j][0] == ' ':
                    line[j] = copy.deepcopy(line[j][1:])
            rows.append(line)
    dataSet = []
    for i in range(len(rows)):
        #print(rows[i])
        for j in range(len(rows[i])):
            number = 0
            index = rows[i][j].find("e")
            number = rows[i][j][0:index]
            exponent = int(rows[i][j][index+1:])
            negativeFlag = False

            if(number[0] == '-'):
                number = number[1:]
                negativeFlag = True

            if(exponent > 0):
                number = float(number)
                for k in range(exponent):
                    number = number * 10.0
            else:
                exponent = abs(exponent)
                index = number.find('.') 
                number = list(number)
                for k in range(exponent):
                    number.insert(0,'0')
                    number[index+1] = number[index]
                    number[index] = '.'
                number = float(''.join(number))
            if (negativeFlag == True):
                number = number * -1
                negativeFlag = False
            rows[i][j] = copy.deepcopy(number)
        dataSet.append(rows[i])
    return (dataSet)
