# Bloxorz Class Implementation
import Block
from queue import PriorityQueue

class Bloxorz:

    def __init__(self, matrix):

        # necessary variables for class functions
        self.board = matrix  # copy board
        self.xLen = len(self.board[0])  # length of x
        self.yLen = len(self.board)  # length of y
        self.startingState = 0
        self.goalPoint = []
    def findStart(self):

        counter = 0

        for y in range(0, self.yLen):  # determine the goal point
            for x in range(0, self.xLen):
                if self.board[y][x] == "G":
                    goalX = x
                    goalY = y
                    break

        self.goalPoint = [goalX, goalY]  # goal coordinate

        for y in range(0, self.yLen):  # determine the block coordinate
            for x in range(0, self.xLen):
                if self.board[y][x] == "S":
                    if counter == 1:
                        self.blockPoint2 = [x, y]  # second point of the block
                        counter += 1
                        break
                    elif counter == 0:
                        self.blockPoint = [x, y]  # first point og the block

                        counter += 1

        if counter == 1:
            self.blockPoint2 = self.blockPoint
            self.player = Block.Player(self.blockPoint, self.blockPoint2, 0)  # state 1 vertical
        elif counter == 2:
            if self.blockPoint[0] != self.blockPoint2[0]:
                self.player = Block.Player(self.blockPoint, self.blockPoint2, 1)  # state 1 horizontal
            else:
                self.player = Block.Player(self.blockPoint, self.blockPoint2, 2)  # state 2 horizontal

    def printBoard(self):

        for y in range(0, self.yLen):
            print(self.board[y])

    def checkTheTile(self, x, y):

        if self.xLen > x >= 0:
            if self.yLen > y >= 0:
                if self.board[y][x] == "X":
                    return False
                else:
                    return True
            return False

    def checkState(self):
        if self.blockPoint == self.blockPoint:
            self.startingState = 0  # vertical
        elif self.blockPoint[0] + 1 == self.blockPoint2[0] or self.blockPoint[0] - 1 == self.blockPoint2[0]:
            self.startingState = 1  # horizontal and parallel to x
        elif self.blockPoint[1] + 1 == self.blockPoint2[1] or self.blockPoint[1] - 1 == self.blockPoint2[1]:
            self.startingState = 2  # horizontal and parallel to y

    def clearOldPoints(self):  # deletes the old player position
        cleanBoard = list(self.board[self.player.currentPoint[1]])
        cleanBoard2 = list(self.board[self.player.currentPoint2[1]])

        cleanBoard[self.player.currentPoint[0]] = "O"
        cleanBoard2[self.player.currentPoint2[0]] = "O"

        self.board[self.player.currentPoint[1]] = "".join(cleanBoard)
        self.board[self.player.currentPoint2[1]] = "".join(cleanBoard2)

    def placeNewPoints(self):  # adds the updated player position

        cleanBoard = list(self.board[self.player.currentPoint[1]])
        cleanBoard2 = list(self.board[self.player.currentPoint2[1]])
        cleanBoard3 = list(self.board[self.goalPoint[1]])

        cleanBoard[self.player.currentPoint[0]] = "S"
        cleanBoard2[self.player.currentPoint2[0]] = "S"
        cleanBoard3[self.goalPoint[0]] = "G"

        self.board[self.player.currentPoint[1]] = "".join(cleanBoard)
        self.board[self.player.currentPoint2[1]] = "".join(cleanBoard2)
        self.board[self.goalPoint[1]] = "".join(cleanBoard3)

    def neighbors(self, current):

        """
        current[0] == coor1
        current[1] == coor2
        current[2] == state
        """

        result = []
        coor1x = current[0][0]
        coor1y = current[0][1]
        coor2x = current[1][0]
        coor2y = current[1][1]

        if current[2] == 0:  # state = 0
            # check up
            if self.checkTheTile(coor1x, coor1y - 1) and self.checkTheTile(coor2x, coor2y - 2):
                result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 2], 2])

            # check down
            if self.checkTheTile(coor1x, coor1y + 1) and self.checkTheTile(coor2x, coor2y + 2):
                result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 2], 2])

            # check left
            if self.checkTheTile(coor1x - 1, coor1y) and self.checkTheTile(coor2x - 2, coor2y):
                result.append([[coor1x - 1, coor1y], [coor2x - 2, coor2y], 1])

            # check right
            if self.checkTheTile(coor1x + 1, coor1y) and self.checkTheTile(coor2x + 2, coor2y):
                 result.append([[coor1x + 1, coor1y], [coor2x + 2, coor2y], 1])

        elif current[2] == 1:  # state = 1
            # check up
            if self.checkTheTile(coor1x, coor1y - 1) and self.checkTheTile(coor2x, coor2y - 1):
                 result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 1], 1])

            # check down
            if self.checkTheTile(coor1x, coor1y + 1) and self.checkTheTile(coor2x, coor2y + 1):
                result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 1], 1])

            if coor2x > coor1x:
                # check left
                if self.checkTheTile(coor1x - 1, coor1y) and self.checkTheTile(coor2x - 2, coor2y):
                    result.append([[coor1x - 1, coor1y], [coor2x - 2, coor2y], 0])

                # check right
                if self.checkTheTile(coor1x + 2, coor1y) and self.checkTheTile(coor2x + 1, coor2y):
                    result.append([[coor1x + 2, coor1y], [coor2x + 1, coor2y], 0])

            else:

                # check left
                if self.checkTheTile(coor1x - 2, coor1y) and self.checkTheTile(coor2x - 1, coor2y):
                    result.append([[coor1x - 2, coor1y], [coor2x - 1, coor2y], 0])

                # check right
                if self.checkTheTile(coor1x + 1, coor1y) and self.checkTheTile(coor2x + 2, coor2y):
                    result.append([[coor1x + 1, coor1y], [coor2x + 2, coor2y], 0])

        elif current[2] == 2:  # state = 2

            if coor2y > coor1y:
                # check up
                if self.checkTheTile(coor1x, coor1y - 1) and self.checkTheTile(coor2x, coor2y - 2):
                    result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 2], 0])

                # check down
                if self.checkTheTile(coor1x, coor1y + 2) and self.checkTheTile(coor2x, coor2y + 1):
                    result.append([[coor1x, coor1y + 2], [coor2x, coor2y + 1], 0])

            else:

                # check up
                if self.checkTheTile(coor1x, coor1y - 2) and self.checkTheTile(coor2x, coor2y - 1):
                    result.append([[coor1x, coor1y - 2], [coor2x, coor2y - 1], 0])

                # check down
                if self.checkTheTile(coor1x, coor1y + 1) and self.checkTheTile(coor2x, coor2y + 2):
                    result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 2], 0])

            # check left
            if self.checkTheTile(coor1x - 1, coor1y) and self.checkTheTile(coor2x - 1, coor2y):
               result.append([[coor1x - 1, coor1y], [coor2x - 1, coor2y], 2])

            # check right
            if self.checkTheTile(coor1x + 1, coor1y) and self.checkTheTile(coor2x + 1, coor2y):
                result.append([[coor1x + 1, coor1y], [coor2x + 1, coor2y], 2])

        return result

    def updateBoard(self, coor1, coor2, state):
        self.clearOldPoints()
        self.player.updatePlayer(coor1, coor2, state)
        self.placeNewPoints()
        self.printBoard()

    def UCS(self):
        q = PriorityQueue()
        goal = [self.goalPoint, self.goalPoint, 0]
        start = [self.player.currentPoint, self.player.currentPoint2, self.player.state]
        visited = {}
        totalCost = {str(start): 0}
        counter = 0

        q.put(start, 0)  # start, total cost
        while not q.empty():
            current = q.get()

            if current == goal:
                print("Solved in :", totalCost[str(goal)], "moves with UCS Algorithm.")
                print()
                path = []
                while current != start:
                    path.append(current)
                    current = visited[str(current)]
                path.append(start)
                path.reverse()
                return path

            for next in self.neighbors(current):
                newCost = totalCost[str(current)] + 1
                if str(next) not in totalCost and str(next) not in visited or newCost < totalCost[str(next)]:
                    totalCost[str(next)] = newCost
                    priority = newCost
                    q.put(next, priority)
                    visited[str(next)] = current
                    counter +=1


    def heuristic(self, next):
        next1x = next[0][0]
        next1y = next[0][1]
        next2x = next[1][0]
        next2y = next[1][1]

        if next[2] == 0:
            distance = abs(self.goalPoint[0] - next1x) + abs(self.goalPoint[1] - next1y)
            return distance
        elif next[2] == 1:
            if self.goalPoint[0]-next1x < self.goalPoint[0]-next2x:
                distance = abs(self.goalPoint[0] - next1x) + abs(self.goalPoint[1] - next1y)
                return distance
            else:
                distance = abs(self.goalPoint[0] - next2x) + abs(self.goalPoint[1] - next2y)
                return distance
        elif next[2] == 2:
            if self.goalPoint[1]-next1y < self.goalPoint[1]-next2y:
                distance = abs(self.goalPoint[0] - next1x) + abs(self.goalPoint[1] - next1y)
                return distance
            else:
                distance = abs(self.goalPoint[0] - next2x) + abs(self.goalPoint[1] - next2y)
                return distance


    def Astar(self):
        q = PriorityQueue()
        goal = [self.goalPoint, self.goalPoint, 0]
        start = [self.player.currentPoint, self.player.currentPoint2, self.player.state]
        visited = {}
        totalCost = {str(start): 0}
        counter = 0

        q.put(start, 0)  # start, total cost
        while not q.empty():
            current = q.get()

            if current == goal:
                print("Solved in :", totalCost[str(goal)], "moves with A* Algorithm.")
                print()

                path = []
                while current != start:
                    path.append(current)
                    current = visited[str(current)]
                path.append(start)
                path.reverse()
                return path

            for next in self.neighbors(current):

                newCost = totalCost[str(current)] + 1

                if str(next) not in totalCost and str(next) not in visited or newCost < totalCost[str(next)]:
                    totalCost[str(next)] = newCost
                    priority = newCost + self.heuristic(next)
                    q.put(next, priority)
                    visited[str(next)] = current
                    counter += 1

    def solution(self, path):
        counter = 0
        for movement in path:
            if counter == 0:
                print("Starting Position, Action: ", counter)
            else:
                print("Action: ", counter)
            self.updateBoard(movement[0], movement[1], movement[2])
            counter += 1
            print()

        print("Done")
        print()