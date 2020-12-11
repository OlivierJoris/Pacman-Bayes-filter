# Complete this class for all parts of the project

from pacman_module.util import manhattanDistance
from pacman_module.game import Agent
from pacman_module.pacman import Directions

import copy


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

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

        stateCopy = copy.deepcopy(state)

        ghostNumber, N, M = belief_state.shape

        maxProba = 0
        coordMaxProba = 0, 0

        # Gets the cell with the highest proba among all the ghosts
        for ghost in range(ghostNumber):

            for x in range(N):
                for y in range(M):
                    if belief_state[ghost][x][y] > maxProba or (belief_state[ghost][x][y] == maxProba and manhattanDistance(stateCopy.getPacmanPosition(), [x,y]) < manhattanDistance(stateCopy.getPacmanPosition(), coordMaxProba)):
                        maxProba = belief_state[ghost][x][y]
                        coordMaxProba = x, y
        
        # We have to look for the move which lead Pacman to the closest 
        # cell of coorMaxProba
        bestAction = None
        minDistance = float('+inf')

        for nextState, action in stateCopy.generatePacmanSuccessors():
            if manhattanDistance(nextState.getPacmanPosition(), coordMaxProba) < minDistance:
                minDistance = manhattanDistance(nextState.getPacmanPosition(), coordMaxProba)
                bestAction = action

        # XXX: End of your code here to obtain bonus

        return bestAction
