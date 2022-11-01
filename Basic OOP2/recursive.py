# N Queen Problem
# Recursive solution

import time

numQueens = 8  # number of queens we are solving for !!!!!!

currentSolution = [0 for x in range(numQueens)]  # will hold current testing data
solutions = []  # found solutions


def isSafe(testRow, testCol):
    # no need to check for row 0
    if testRow == 0:
        return True

    for row in range(0, testRow):

        # check vertical
        if testCol == currentSolution[row]:
            return False

        # diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    # no attack found
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                #  last row
                solutions.append(currentSolution.copy())
                print( "Solution number ", len( solutions ), currentSolution )
            else:
                placeQueen(row + 1)

print("Solving for " + str(numQueens) + " Queens")

time.sleep(2)
placeQueen(0)

print(len(solutions), " solutions found")
for solution in solutions:
    print(solution)
