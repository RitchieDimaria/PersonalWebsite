
tlist = []
import copy
def solve(table):
    for row in range(0,9):
        for col in range(0,9):
            if table[row][col] == 0:
                for number in range(1,10):
                    if valuePossible(table,row,col,number):
                        table[row][col] = number
                        solve(table)
                        table[row][col] = 0
                return
    x = copy.deepcopy(table)
    tlist.append(x)
    if (len(tlist) > 9):
        raise Exception ("Going to exceed 10 known solutions") 



def valuePossible(table, row , col, val):
    for i in range(0,9):
        if table[row][i] == val:
            return False
    
    for i in range(0,9):
        if table[i][col] == val:
            return False
    
    x = (col//3) *3
    y = (row//3) *3
    for i in range(0,3):
        for j in range(0,3):
            if table[y+i][x+j] == val:
                return False
    return True

def findAllTables(table):
    global tlist
    tlist = []
    try:
        solve(table)
        moreSolutions = False
    except Exception as e:
        moreSolutions = True
    
    return(tlist,moreSolutions)