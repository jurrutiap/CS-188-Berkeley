# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node:
    def __init__(self, coords: tuple, parent, direc: str, priority: int=None):
        self.coords =  coords
        self.parent = parent
        self.parent_direction = direc
        self.priority = priority

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    visited = []
    start_node = Node(problem.getStartState(), None, None)
    stack = util.Stack()

    stack.push(start_node)

    while not stack.isEmpty():
        current_node = stack.pop()
        visited.append(current_node.coords)
        if problem.isGoalState(current_node.coords):
            break
        for coords in problem.getSuccessors(current_node.coords):
            if coords[0] not in visited:
                stack.push(Node(coords[0], current_node, coords[1]))

    return_path = []

    while current_node.parent is not None:
        return_path.insert(0, current_node.parent_direction)
        current_node = current_node.parent

    return return_path

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    start_node = Node(problem.getStartState(), None, None)
    queue = util.Queue()

    queue.push(start_node)
    visited.append(start_node.coords)

    while not queue.isEmpty():
        current_node = queue.pop()
        visited.append(current_node.coords)
        if problem.isGoalState(current_node.coords):
            break
        for coords in problem.getSuccessors(current_node.coords):
            if coords[0] not in visited:
                queue.push(Node(coords[0], current_node, coords[1]))
                visited.append(coords[0])

    return_path = []

    while current_node.parent is not None:
        return_path.insert(0, current_node.parent_direction)
        current_node = current_node.parent

    return return_path

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = {}
    start_node = Node(problem.getStartState(), None, None, 0)
    pqueue = util.PriorityQueue()

    pqueue.push(start_node, start_node.priority)

    while not pqueue.isEmpty():
        current_node = pqueue.pop()
        visited[current_node.coords] = current_node
        if problem.isGoalState(current_node.coords):
            break
        for coords in problem.getSuccessors(current_node.coords):
            if coords[0] not in visited.keys():
                new_node = Node(coords[0], current_node, coords[1], current_node.priority + coords[2])
                visited[new_node.coords] = new_node
                pqueue.push(new_node, new_node.priority)
            else:
                revisited_node = visited[coords[0]]
                if revisited_node.priority > current_node.priority + coords[2]:
                    new_node = Node(revisited_node.coords, current_node, coords[1], current_node.priority + coords[2])
                    pqueue.push(new_node, new_node.priority)

    return_path = []

    while current_node.parent is not None:
        return_path.insert(0, current_node.parent_direction)
        current_node = current_node.parent

    return return_path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
