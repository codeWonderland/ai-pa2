"""
Author: Alice Easter && Sam LoPiccolo
Class: CSI-480-01
Assignment: PA 2 -- Search
Due Date: September 26, 2018 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

----------------------
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
import copy

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


def graph_search(problem, fringe):
    closed = set()

    # we know that we aren't starting at the goal,
    # so we start by putting the successors of the start state 
    # on the fringe
    for state in problem.get_successors(problem.get_start_state()):
        # the nodes are being placed in an array as the fringe
        # is keeping track of the path, not just the individual nodes
        # it just so happens that this is a path with only one step
        fringe.push([state]) 
    
    while not fringe.is_empty():

        # grap the next path to explore on the fringe
        path = fringe.pop()
        
        # the last element in the path is the newest node
        # and we need to check it's state
        state = path[-1][0]

        # should we be adding the whole path here?
        if state not in closed:
            closed.add(state)

            if problem.is_goal_state(state):
                break

            # while we are already iterating over the new nodes
            # we should make sure that we haven't explored any 
            # of them already
            successors = [node for node in problem.get_successors(state) if node[0] not in closed]

            for node in successors:
                # create a new path based off of what we have just explored
                tmp_path = copy.deepcopy(path)
                
                # add the new node to explore to the end of said path
                tmp_path.append(node)

                fringe.push(tmp_path)

    # we only need the directions we are going
    # so we are just returning that part of our path
    return [state[1] for state in path]


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
    return graph_search(problem, util.Stack())


def breadth_first_search(problem):
    """Run BFS on the given problem."""
    return graph_search(problem, util.Queue())


def uniform_cost_search(problem):
    """Run UCS on the given problem."""
    def calc_cost(path):
        return problem.get_cost_of_actions([node[1] for node in path])
    
    return graph_search(problem, util.PriorityQueueWithFunction(calc_cost))


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
    def calc_cost(path):
        return problem.get_cost_of_actions([node[1] for node in path]) + \
            heuristic(path[-1][0], problem)
    
    return graph_search(problem, util.PriorityQueueWithFunction(calc_cost))


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
a_star = a_star_search
ucs = uniform_cost_search
