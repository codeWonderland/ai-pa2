"""Here you will implement generic search algorithms.

Champlain College CSI-480, Fall 2018
The following code was adapted by Joshua Auerbach (jauerbach@champlain.edu)
from the UC Berkeley Pacman Projects (see license and attribution below).

----------------------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""

import util


class SearchProblem:
    """This class outlines the structure of a search problem.

    Note this class does not implement any of the methods
    (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """Return the start state for the search problem."""
        util.raise_not_defined()

    def is_goal_state(self, state):
        """Return True if and only if the state is a valid goal state."""
        util.raise_not_defined()

    def get_successors(self, state):
        """Return list of successors from given state.

        Return:
            List of triples: (successor, action, step_cost),
            where 'successor' is a successor to the current state,
            'action' is the action required to get there, and 'step_cost' is
            the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """Return the total cost of a particular sequence of actions.

        Args:
            actions: A list of actions to take

        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


def tiny_maze_search(problem):
    """Return a sequence of moves that solves tiny_maze.

    For any other maze, the sequence of moves will be incorrect,
    so only use this for tiny_maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
    """Run DFS on the given problem.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.get_start_state())
    print("Is the start a goal?",
          problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:",
          problem.get_successors(problem.get_start_state()))
    """

    fringe = problem.get_successors(problem.get_start_state())
    closed = set()
    path = []

    # a node should represent the path to itself
    # a state should be the current position of the node

    while len(fringe):
        node = fringe.pop()
        path.append(node[1])
        print(path)

        if problem.is_goal_state(node[0]):
            break

        if (node, ','.join(path)) not in closed:
            closed.add((node, ','.join(path)))

            successors = problem.get_successors(node[0])

            if (len(successors)):
                fringe.extend(successors)
            else:
                path.pop()

    return path

def breadth_first_search(problem):
    """Run BFS on the given problem."""
    # *** YOUR CODE HERE ***
    util.raise_not_defined()


def uniform_cost_search(problem):
    """Run UCS on the given problem."""
    # *** YOUR CODE HERE ***
    util.raise_not_defined()


def null_heuristic(state, problem=None):
    """Return a trivial heuristic.

    In general a heuristic function estimates the cost from the current state
    to the nearest goal in the provided SearchProblem.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """Run A* on the given problem.

    A* searches the node that has the lowest combined cost and heuristic first.
    """
    # *** YOUR CODE HERE ***
    util.raise_not_defined()


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
a_star = a_star_search
ucs = uniform_cost_search
