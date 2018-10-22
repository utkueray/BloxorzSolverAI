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

    def findStart(self):

        counter = 0

        for y in range(0, self.yLen):  # determine the goal point
            for x in range(0, self.xLen):
                if self.board[y][x] == "G":
                    goalX = x
                    goalY = y
                    break

        self.goalPoint = [goalX, goalY]  # goal coordinate

        print("Goal Point: ", self.goalPoint)

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

        print()

        if counter == 1:
            self.blockPoint2 = self.blockPoint
            self.player = Block.Player(self.blockPoint, self.blockPoint2, 0)  # state 1 vertical
            print("Player Coordinates: ", self.blockPoint)
            print("Vertical")

        elif counter == 2:
            if self.blockPoint[0] != self.blockPoint2[0]:
                self.player = Block.Player(self.blockPoint, self.blockPoint2, 1)  # state 1 horizontal
                print("Player Coordinates: ", self.blockPoint, self.blockPoint2)
                print("Horizontal and Parallel to X")

            else:
                self.player = Block.Player(self.blockPoint, self.blockPoint2, 2)  # state 2 horizontal
                print("Player Coordinates: ", self.blockPoint, self.blockPoint2)
                print("Horizontal and Parallel to Y")

    def printBoard(self):

        for y in range(0, self.yLen):
            print(self.board[y])

    def checkTheTile(self, x, y):
        #index out of range error

        if self.board[y][x] == "X":
            return False
        elif self.board[y][x] == "G" and self.player.state == 0:
            print("Goal")
        else:
            return True

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

    def move(self, direction):
        x1 = self.player.currentPoint[0]
        y1 = self.player.currentPoint[1]
        x2 = self.player.currentPoint2[0]
        y2 = self.player.currentPoint2[1]

        if self.player.state == 0:  # vertical
            if direction == "U" or direction == "D":  # player state will be 2
                if direction == "U":
                    print("moving up")
                    y1 -= 1
                    y2 -= 2

                elif direction == "D":
                    print("moving down")
                    y1 += 1
                    y2 += 2

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 2]

            if direction == "L" or direction == "R":  # player state will be 1
                if direction == "R":
                    print("moving right")
                    x1 += 1
                    x2 += 2

                elif direction == "L":
                    print("movign left")
                    x1 -= 1
                    x2 -= 2

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 1]

        elif self.player.state == 1:  # horizontal 1
            if direction == "U" or direction == "D":  # player state will be 1
                if direction == "U":
                    print("moving up")
                    y1 -= 1
                    y2 -= 1

                elif direction == "D":
                    print("moving down")
                    y1 += 1
                    y2 += 1

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 1]

            if direction == "L" or direction == "R":  # player state will be 0
                if direction == "R":
                    print("moving right")
                    if x1 > x2:
                        x1 += 1
                        x2 = x1
                    else:
                        x2 += 1
                        x1 = x2

                elif direction == "L":
                    print("moving left")
                    if x1 < x2:
                        x1 -= 1
                        x2 = x1
                    else:
                        x2 -= 1
                        x1 = x2

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 0]

        elif self.player.state == 2:  # horizontal 2
            if direction == "U" or direction == "D":  # player state will be 1
                if direction == "U":
                    print("moving up")
                    if y1 < y2:
                        y1 -= 1
                        y2 = y1
                    else:
                        y2 -= 1
                        y1 = y2

                elif direction == "D":
                    print("moving down")

                    if y1 > y2:
                        y1 += 1
                        y2 = y1
                    else:
                        y2 += 1
                        y1 = y2

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 0]

            if direction == "L" or direction == "R":  # player state will be 0
                if direction == "R":
                    print("moving right")
                    x1 += 1
                    x2 += 1

                elif direction == "L":
                    print("moving left")
                    x1 -= 1
                    x2 -= 1

                if self.checkTheTile(x1, y1):
                    if self.checkTheTile(x2, y2):
                        result = [[x1, y1], [x2, y2], 2]

        return result

    def movePlayer(self, direction):
        self.clearOldPoints()

        print("---------------")

        self.move(direction)

        if self.player.state == 0:
            print("Block At: ", self.player.currentPoint)
        else:
            print("Block At: ", self.player.currentPoint, self.player.currentPoint2)

        self.placeNewPoints()
        print()
        self.printBoard()

        if self.player.state == 0 and self.player.currentPoint == self.goalPoint:
            print("The End")

    def hashx(self, obj):

        coor1x = obj[0][0]
        coor1y = obj[0][1]
        coor2x = obj[1][0]
        coor2y = obj[1][1]

        hashx = ((len(self.board) * len(self.board[0]) * obj[2]) + (len(self.board[0]) * coor1y)) + coor2x

        return hashx

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
            if self.checkTheTile(coor1x, coor1y - 1):
                if self.checkTheTile(coor2x, coor2y - 2):
                    result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 2], 2])

            # check down
            if self.checkTheTile(coor1x, coor1y + 1):
                if self.checkTheTile(coor2x, coor2y + 2):
                    result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 2], 2])

            # check left
            if self.checkTheTile(coor1x - 1, coor1y):
                if self.checkTheTile(coor2x - 2, coor2y):
                    result.append([[coor1x - 1, coor1y], [coor2x - 2, coor2y], 1])

            # check right
            if self.checkTheTile(coor1x + 1, coor1y):
                if self.checkTheTile(coor2x + 2, coor2y):
                    result.append([[coor1x + 1, coor1y], [coor2x + 2, coor2y], 1])

        elif current[2] == 1:  # state = 1
            # check up
            if self.checkTheTile(coor1x, coor1y - 1):
                if self.checkTheTile(coor2x, coor2y - 1):
                    result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 1], 1])

            # check down
            if self.checkTheTile(coor1x, coor1y + 1):
                if self.checkTheTile(coor2x, coor2y + 1):
                    result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 1], 1])

            # check left
            if self.checkTheTile(coor1x - 1, coor1y):
                if self.checkTheTile(coor2x - 2, coor2y):
                    result.append([[coor1x - 1, coor1y], [coor2x - 2, coor2y], 0])

            # check right
            if self.checkTheTile(coor1x + 1, coor1y):
                if self.checkTheTile(coor2x + 2, coor2y):
                    result.append([[coor1x + 1, coor1y], [coor2x + 2, coor2y], 0])

        elif current[2] == 2:  # state = 2
            # check up
            if self.checkTheTile(coor1x, coor1y - 1):
                if self.checkTheTile(coor2x, coor2y - 2):
                    result.append([[coor1x, coor1y - 1], [coor2x, coor2y - 2], 0])

            # check down
            if self.checkTheTile(coor1x, coor1y + 1):
                if self.checkTheTile(coor2x, coor2y + 2):
                    result.append([[coor1x, coor1y + 1], [coor2x, coor2y + 2], 0])
            # check left
            if self.checkTheTile(coor1x - 1, coor1y):
                if self.checkTheTile(coor2x - 1, coor2y):
                    result.append([[coor1x - 1, coor1y], [coor2x - 1, coor2y], 2])

            # check right
            if self.checkTheTile(coor1x + 1, coor1y):
                if self.checkTheTile(coor2x + 1, coor2y):
                    result.append([[coor1x + 1, coor1y], [coor2x + 1, coor2y], 2])

        if current[0] == self.goalPoint and current[1] == self.goalPoint:
        print(result)
        return result

    def UCS(self):
        print("---------------")
        self.findStart()
        print()
        print("Starting...")
        print()
        self.checkState()

        queue = PriorityQueue()
        goal = [self.goalPoint, self.goalPoint, 0]
        start = [self.player.currentPoint, self.player.currentPoint2, self.player.state]
        visited = [str(start)]
        totalCost = {str(start): 0}

        queue.put(start, 0)  # start, total cost
        while not queue.empty():
            current = queue.get()

            if current == goal:
                print("Finished")
                self.printBoard()
                break

            for next in self.neighbors(current):
                self.printBoard()
                print()
                newCost = totalCost[str(current)] + 1
                print(newCost)

                if str(next) not in totalCost and str(next) not in visited or newCost < totalCost[str(next)]:
                    totalCost[str(next)] = newCost
                    priority = newCost
                    queue.put(next, priority)
                    crt = str(current)
                    visited.append(str(next))
                    print()
                    self.clearOldPoints()
                    self.player.updatePlayer(next[0], next[1], next[2])
                    self.placeNewPoints()