
# AI Assignment#1 - Solve Bloxorz with A* Search Algorithm

import Bloxorz as Bz
from datetime import datetime
import os
import psutil

file = open('test3.txt', 'r') # open board files
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
problem.findStart()
problem2.findStart()
problem.checkState()
problem2.checkState()
print("Goal Coordinate:", problem.goalPoint)
if problem.startingState == 0:
    print("Player Coordinate: ", problem.blockPoint)
    print("Starting Vertical")
elif problem.startingState == 1:
    print("Player Coordinates: ", problem.blockPoint, problem.blockPoint2)
    print("Starting Horizontal and Parallel to X")
elif problem.startingState == 2:
    print("Player Coordinates: ", problem.blockPoint, problem.blockPoint2)
    print("Starting Horizontal and Parallel to Y")
print()
process = psutil.Process(os.getpid())

start_time = datetime.now()
ucsResult = problem.UCS()
problem.solution(ucsResult)
end_time = datetime.now()

print("----------------------------------------------")

start_time2 = datetime.now()
process2 = psutil.Process(os.getpid())
astarResult = problem2.Astar()
problem2.solution(astarResult)
end_time2 = datetime.now()

print("Results:")
print("----------------------------------")
print("UCS Time and Memory Usage")
print('Duration: {}'.format(end_time.microsecond - start_time.microsecond), "MicroSeconds")
print("Memory:", process.memory_percent().__round__(5), "%")
print()
print("A* Time and Memory Usage")
print("Memory:", process2.memory_percent().__round__(5), "%")
print('Duration: {}'.format(end_time2.microsecond - start_time2.microsecond), "MicroSeconds")
