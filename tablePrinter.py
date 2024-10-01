tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colwidths = [0] * len(tableData)
    for index, row in enumerate(tableData):
        for word in row:
            if colwidths[index] == 0:
                colwidths[index] = len(word)
            else:
                currWordLen = len(word)
                if currWordLen > colwidths[index]:
                    colwidths[index] = currWordLen

    print(tableData[0][0].rjust(colwidths[0]))
    print(tableData[1][0].rjust(colwidths[1]))
    print(tableData[2][0].rjust(colwidths[2]) + "\n")
    print(tableData[0][1].rjust(colwidths[0]))
    print(tableData[1][1].rjust(colwidths[1]))
    print(tableData[2][1].rjust(colwidths[2]) + "\n")
    print(tableData[0][2].rjust(colwidths[0]))
    print(tableData[1][2].rjust(colwidths[1]))
    print(tableData[2][2].rjust(colwidths[2]))
    print(tableData[0][3].rjust(colwidths[0]))
    print(tableData[1][3].rjust(colwidths[1]))
    print(tableData[2][3].rjust(colwidths[2]))
        

printTable()