class Player:

    def __init__(self, startCoor1, startCoor2, state):
        # vertical if state = 0
        # horizontal constructor, if state = 1 then its parallel to x, if state = 2 then its parallel to y

        self.currentPoint = startCoor1
        self.currentPoint2 = startCoor2
        self.state = state

    def updatePlayer(self, newCoor1, newCoor2, state): # update player data
        self.currentPoint = newCoor1
        self.currentPoint2 = newCoor2
        self.state = state
