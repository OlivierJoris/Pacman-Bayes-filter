# Complete this class for all parts of the project

from pacman_module.util import manhattanDistance
from pacman_module.game import Agent
from pacman_module.pacman import Directions


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.mazeCost = None
    
    def computeMazeCost(self, currentCoords, state, N, M, closed):
        """
        Computes the cost of each cell in the maze to reach [currentCoords] from
        the current Pacman position until reaching it.

        Arguments:
        ----------
        - `currentCoords`: a list of coordinates we want to compute their neighbor costs.
        - `state`: the current state of the maze.
        - `N`: the width of the maze.
        - `N`: the height of the maze.
        - 'closed' : a set maintaining the cells coordinates that the cost has already been
        computed.

        """
        # Coordinates for the recursive call
        recCoords = []

        for currentCoord in currentCoords:
            # If we arrive to the Pacman position we can stop the recursion
            if currentCoord[0] == state.getPacmanPosition()[0] and \
               currentCoord[1] == state.getPacmanPosition()[1]:
                return

            for neighborX in range(currentCoord[0] - 1, currentCoord[0] + 2):
                for neighborY in range(currentCoord[1] - 1, currentCoord[1] + 2):
                    # Check if we are not exiting the maze or exploring a cell already
                    # explored
                    if  (neighborX not in range(N))\
                     or (neighborY not in range(M))\
                     or (neighborX, neighborY) in closed:
                        continue

                    # Updating the cost of the cell in the maze
                    elif not state.getWalls()[neighborX][neighborY]:
                        self.mazeCost[neighborX][neighborY] = self.mazeCost[currentCoord[0]][currentCoord[1]] + 1
                        recCoords.append([neighborX, neighborY])
                        closed.add((neighborX, neighborY))

        return self.computeMazeCost(recCoords, state, N, M, closed)

    def get_action(self, state, belief_state):
        """
        Given a pacman game state and a belief state,
                returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.
        - `belief_state`: a list of probability matrices.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        # XXX: Your code here to obtain bonus

        stateCopy = state.deepCopy()

        ghostNumber, N, M = belief_state.shape

        maxProba = 0
        coordMaxProba = [0, 0]

        ghosts_eaten = stateCopy.data._eaten[1:]

        # We chase the ghosts one per one to save time and 
        # get a higher score
        for ghost in range(ghostNumber):
            if not ghosts_eaten[ghost]:
                currentChasedGhostIndex = ghost

        # Gets the cell of the coordinates with the higher probability
        for x in range(N):
            for y in range(M):
                if belief_state[currentChasedGhostIndex][x][y] > maxProba or \
                (belief_state[currentChasedGhostIndex][x][y] >= maxProba and \
                manhattanDistance(stateCopy.getPacmanPosition(), [x,y])\
                < manhattanDistance(stateCopy.getPacmanPosition(), coordMaxProba)):
                    maxProba = belief_state[currentChasedGhostIndex][x][y]
                    coordMaxProba = x, y

        closed = set()

        self.mazeCost = [[float('+inf') for m in range(M)] for n in range(N)]

        self.mazeCost[coordMaxProba[0]][coordMaxProba[1]] = 0

        self.computeMazeCost([coordMaxProba], stateCopy, N, M, closed)

        bestAction = stateCopy.getLegalActions()[0]

        bestCost = float('+inf')

        for nextState, action in stateCopy.generatePacmanSuccessors():
            if self.mazeCost[nextState.getPacmanPosition()[0]][nextState.getPacmanPosition()[1]] < bestCost:
                bestAction = action
                bestCost = self.mazeCost[nextState.getPacmanPosition()[0]][nextState.getPacmanPosition()[1]]

        # XXX: End of your code here to obtain bonus

        return bestAction
