# Complete this class for all parts of the project

from pacman_module.game import Agent
import numpy as np
from pacman_module import ghostAgents, util
from scipy.stats import binom
import math


class BeliefStateAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        """
            Variables to use in 'update_belief_state' method.
            Initialization occurs in 'get_action' method.
        """
        # Current list of belief states over ghost positions
        self.beliefGhostStates = None

        # Grid of walls (assigned with 'state.getWalls()' method)
        self.walls = None

        # Hyper-parameters
        self.ghost_type = self.args.ghostagent
        self.sensor_variance = self.args.sensorvariance

        self.p = 0.5
        self.n = int(self.sensor_variance/(self.p*(1-self.p)))

    def ghostTransition(
        self, mazeWidth, mazeHeight, currentPos, previousPos, pacman_position
    ):
        """
        Returns the probability for a ghost to go from previousPos
        to currentPos.

        Arguments:
        ----------
        - `mazeWidth`: the width of the maze
        - `mazeHeight`: the height of the maze
        - `currentPos`: 2D coordinates position
          of a ghost at state x_{t}
          where 't' is the current time step.
        - `previousPos`: 2D coordinates possible position
          of a ghost at state x_{t - 1}
          where 't' is the current time step
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step

        Return:
        -------
        - The probability for a ghost to go from previousPos to currentPos
        """

        currX = currentPos[0]
        currY = currentPos[1]
        prevX = previousPos[0]
        prevY = previousPos[1]

        # Go through a wall is not a legal action
        if self.walls[currX][currY] or self.walls[prevX][prevY]:
            return 0

        # Stay on the same cell is not a legal action
        if currentPos == previousPos:
            return 0

        # The ghost can only go to vertical and horizontal neighbor cells
        if (prevX - 1 == currX and prevY + 1 == currY) \
                or (prevX - 1 == currX and prevY - 1 == currY) \
                or (prevX + 1 == currX and prevY + 1 == currY) \
                or (prevX + 1 == currX and prevY - 1 == currY):

            return 0

        nbLegalActions = 0

        # Check if it is not a wall on the cell he can go
        if not self.walls[prevX + 1][prevY] and prevX + 1 < mazeWidth:
            nbLegalActions += 1

        if not self.walls[prevX - 1][prevY] and prevX - 1 > 0:
            nbLegalActions += 1

        if not self.walls[prevX][prevY + 1] and prevY + 1 < mazeHeight:
            nbLegalActions += 1

        if not self.walls[prevX][prevY - 1] and prevY - 1 > 0:
            nbLegalActions += 1

        gamma = 1

        currDistance = util.manhattanDistance(currentPos, pacman_position)
        prevDistance = util.manhattanDistance(previousPos, pacman_position)

        if currDistance >= prevDistance:
            if self.ghost_type == "afraid":
                gamma = 2
            elif self.ghost_type == "scared":
                gamma = 8

        transitionProba = gamma / (gamma * nbLegalActions)

        return transitionProba

    def update_belief_state(self, evidences, pacman_position, ghosts_eaten):
        """
        Given a list of (noised) distances from pacman to ghosts,
        returns a list of belief states about ghosts positions

        Arguments:
        ----------
        - `evidences`: list of distances between
          pacman and ghosts at state x_{t}
          where 't' is the current time step
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step
        - `ghosts_eaten`: list of booleans indicating
          whether ghosts have been eaten or not

        Return:
        -------
        - A list of Z belief states at state x_{t}
          as N*M numpy mass probability matrices
          where N and M are respectively width and height
          of the maze layout and Z is the number of ghosts.

        N.B. : [0,0] is the bottom left corner of the maze.
               Matrices filled with zeros must be returned for eaten ghosts.
        """
        beliefStates = self.beliefGhostStates

        # XXX: Your code here

        sensorStandardDeviation = math.sqrt(self.sensor_variance)

        ghostNumber, N, M = beliefStates.shape

        for ghost in range(ghostNumber):
            if not ghosts_eaten[ghost]:

                # Initialize the belief states
                for x in range(N):
                    for y in range(M):
                        beliefStates[ghost][x][y] = 1 / (N * M)

                sensorDistance = evidences[ghost]

                distanceRange = [
                    sensorDistance - sensorStandardDeviation,
                    sensorDistance + sensorStandardDeviation
                ]

                normalizationFactor = 0

                for x in range(N):
                    for y in range(M):
                        distanceToPacman = math.sqrt(
                            (x - pacman_position[0]) ** 2 +
                            (y - pacman_position[1]) ** 2
                        )

                        # Distance too small or too high seeing the one
                        # of the rusty sensor
                        if distanceToPacman < distanceRange[0] or\
                                distanceToPacman > distanceRange[1]:
                            beliefStates[ghost][x][y] = 0

                        else:
                            totalProba = 0

                            for possiblePreviousX in range(x - 1, x + 2):
                                for possiblePreviousY in range(y - 1, y + 2):
                                    # Check if we are not exiting the maze by
                                    # exploring the neighbor cells
                                    if possiblePreviousX not in range(N)\
                                            or possiblePreviousY\
                                            not in range(M):
                                        continue
                                    else:
                                        currValue = (
                                            self.beliefGhostStates[ghost]
                                            [possiblePreviousX]
                                            [possiblePreviousY]
                                        )
                                        update = self.ghostTransition(
                                            N, M, [x, y],
                                            [
                                                possiblePreviousX,
                                                possiblePreviousY
                                            ],
                                            pacman_position
                                        )

                                        totalProba += currValue * update

                            beliefStates[ghost][x][y] *= totalProba

                        normalizationFactor += beliefStates[ghost][x][y]

                for x in range(N):
                    for y in range(M):
                        if normalizationFactor != 0:
                            beliefStates[ghost][x][y] /= normalizationFactor

        # XXX: End of your code

        self.beliefGhostStates = beliefStates

        return beliefStates

    def _get_evidence(self, state):
        """
        Computes noisy distances between pacman and ghosts.

        Arguments:
        ----------
        - `state`: The current game state s_t
                   where 't' is the current time step.
                   See FAQ and class `pacman.GameState`.


        Return:
        -------
        - A list of Z noised distances in real numbers
          where Z is the number of ghosts.

        XXX: DO NOT MODIFY THIS FUNCTION !!!
        Doing so will result in a 0 grade.
        """
        positions = state.getGhostPositions()
        pacman_position = state.getPacmanPosition()
        noisy_distances = []

        for pos in positions:
            true_distance = util.manhattanDistance(pos, pacman_position)
            noise = binom.rvs(self.n, self.p) - self.n*self.p
            noisy_distances.append(true_distance + noise)

        return noisy_distances

    def _record_metrics(self, belief_states, state):
        """
        Use this function to record your metrics
        related to true and belief states.
        Won't be part of specification grading.

        Arguments:
        ----------
        - `state`: The current game state s_t
                   where 't' is the current time step.
                   See FAQ and class `pacman.GameState`.
        - `belief_states`: A list of Z
           N*M numpy matrices of probabilities
           where N and M are respectively width and height
           of the maze layout and Z is the number of ghosts.

        N.B. : [0,0] is the bottom left corner of the maze
        """
        pass

    def get_action(self, state):
        """
        Given a pacman game state, returns a belief state.

        Arguments:
        ----------
        - `state`: the current game state.
                   See FAQ and class `pacman.GameState`.

        Return:
        -------
        - A belief state.
        """

        """
           XXX: DO NOT MODIFY THAT FUNCTION !!!
                Doing so will result in a 0 grade.
        """
        # Variables are specified in constructor.
        if self.beliefGhostStates is None:
            self.beliefGhostStates = state.getGhostBeliefStates()
        if self.walls is None:
            self.walls = state.getWalls()

        evidence = self._get_evidence(state)
        newBeliefStates = self.update_belief_state(evidence,
                                                   state.getPacmanPosition(),
                                                   state.data._eaten[1:])
        self._record_metrics(self.beliefGhostStates, state)

        return newBeliefStates, evidence
