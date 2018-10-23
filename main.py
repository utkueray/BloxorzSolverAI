
# AI Assignment#1 - Solve Bloxorz with A* Search Algorithm

import Bloxorz as Bz

file = open('board.txt', 'r') # open board files
boardData = [] # empty array to bi filled with data later
boardData2 = [] # empty array to bi filled with data later

while True:
    line = file.readline()
    if line == '':
        break
    boardData.append(line.strip())
    boardData2.append(line.strip())

file.close() # close file

problem = Bz.Bloxorz(boardData) # construct a game object
problem2 = Bz.Bloxorz(boardData2)
problem.UCS()

problem2.Astar()
