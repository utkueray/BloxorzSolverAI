
# AI Assignment#1 - Solve Bloxorz with A* Search Algorithm

import Bloxorz as Bz
from datetime import datetime
import os
import psutil

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
process = psutil.Process(os.getpid())

start_time = datetime.now()
problem.UCS()
end_time = datetime.now()
print("Memory:", process.memory_info().rss)
print('Duration: {}'.format(end_time - start_time))

start_time2 = datetime.now()
process2 = psutil.Process(os.getpid())
problem2.Astar()
end_time = datetime.now()
print("Memory:", process2.memory_info().rss)
print('Duration: {}'.format(end_time - start_time2))
