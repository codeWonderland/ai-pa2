# ai-pa2
A collection of search algorithms for pa2 in my ai class

pa2 def:


Introduction

In this project, your Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. You will build general search algorithms and apply them to Pacman scenarios.

As in the Python Practice assignment, this project includes an autograder for you to grade your answers on your machine. This can be run with the command:

python autograder.py

See the Python Practice for more information about using the autograder.

The code for this project consists of several Python files, some of which you will need to read and understand in order to complete the assignment, and some of which you can ignore. You can download all the code and supporting files as a zip archive: search.zip

Files you'll edit:
search.py 	Where all of your search algorithms will reside.
search_agents.py 	Where all of your search-based agents will reside.
Files you might want to look at:
pacman.py 	The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project.
game.py 	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.
util.py 	Useful data structures for implementing search algorithms.
Supporting files you can ignore:
graphics_display.py 	Graphics for Pacman
graphics_utils.py 	Support for Pacman graphics
text_display.py 	ASCII graphics for Pacman
ghost_agents.py 	Agents to control ghosts
keyboard_agents.py 	Keyboard interfaces to control Pacman
layout.py 	Code for reading layout files and storing their contents
autograder.py 	Project autograder
test_parser.py 	Parses autograder test and solution files
test_classes.py 	General autograding test classes
test_cases/ 	Directory containing the test cases for each question
search_test_classes.py 	PA 2 specific autograding test classes
grading.py 	Autograder code
project_params.py 	Project parameters
pacman_agents.py 	Basic Pacman agents
eight_puzzle.py 	Eight Puzzle classes and utilities

 

Files to Edit and Submit: You will fill in portions of search.py and search_agents.py during the assignment. You should submit these files with your code and comments. Please do not change the other files in this distribution or submit any of the other original files other than these files.

Evaluation: Your code will be autograded for technical correctness. Please do not change the names of any provided functions or classes within the code, or you will wreak havoc on the autograder. However, the correctness of your implementation -- not the autograder's judgements -- will be the final judge of your score.

Academic Dishonesty: I will be checking your code against other submissions in the class for logical redundancy. If you copy someone else's code and submit it with minor changes, we will know. These cheat detectors are quite hard to fool, so please don't try. I trust you all to submit your own work only; please don't let me down. If you do, I will pursue the strongest consequences available.

Getting Help: You are not alone! If you find yourself stuck on something, discuss with your classmates and contact me for help (jauerbach@champlain.edu).  Remember I have office hours T,Th 3:30-5:30. I want these projects to be rewarding and instructional, not frustrating and demoralizing. But, I don't know when or how to help unless you ask.

Discussion: Discussion is encouraged, but please do not share solutions or post solutions publicly.
Welcome to Pacman

After downloading the code search.zip, unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:

python pacman.py

Pacman lives in a shiny blue world of twisting corridors and tasty round treats. Navigating this world efficiently will be Pacman's first step in mastering his domain.

The simplest agent in search_agents.py is called the GoWestAgent, which always goes West (a trivial reflex agent). This agent can occasionally win:

python pacman.py --layout test_maze --pacman GoWestAgent

But, things get ugly for this agent when turning is required:

python pacman.py --layout tiny_maze --pacman GoWestAgent

If Pacman gets stuck, you can exit the game by typing CTRL-c into your terminal.

Soon, your agent will solve not only tiny_maze, but any maze you want.

Note that pacman.py supports a number of options that can each be expressed in a long way (e.g., --layout) or a short way (e.g., -l). You can see the list of all options and their default values via:

python pacman.py -h

Also, all of the commands that appear in this project also appear in commands.txt, for easy copying and pasting. In UNIX/Mac OS X, you can even run all these commands in order with bash commands.txt.
Question 1 (12 points): Finding a Fixed Food Dot using Depth First Search

In search_agents.py, you'll find a fully implemented SearchAgent, which plans out a path through Pacman's world and then executes that path step-by-step. The search algorithms for formulating a plan are not implemented -- that's your job.

First, test that the SearchAgent is working correctly by running:

python pacman.py -l tiny_maze -p SearchAgent -a fn=tiny_maze_search

The command above tells the SearchAgent to use tiny_maze_search as its search algorithm, which is implemented in search.py. Pacman should navigate the maze successfully.

Now it's time to write full-fledged generic search functions to help Pacman plan routes! Pseudocode for the search algorithms you'll write can be found in the lecture slides. Remember that a search node must contain not only a state but also the information necessary to reconstruct the path (plan) which gets to that state.

Important note: All of your search functions need to return a list of actions that will lead the agent from the start to the goal. These actions all have to be legal moves (valid directions, no moving through walls).

Important note: Make sure to use the Stack, Queue and PriorityQueue data structures provided to you in util.py! These data structure implementations have particular properties which are required for compatibility with the autograder.

Hint: Each algorithm is very similar. Algorithms for DFS, BFS, UCS, and A* differ only in the details of how the fringe is managed. So, concentrate on getting DFS right and the rest should be relatively straightforward. Indeed, one possible implementation requires only a single generic search method which is configured with an algorithm-specific queuing strategy. (Your implementation need not be of this form to receive full credit).

Implement the depth-first search (DFS) algorithm in the depth_first_search function in search.py. To make your algorithm complete, write the graph search version of DFS, which avoids expanding any already visited states.

Your code should quickly find a solution for:

python pacman.py -l tiny_maze -p SearchAgent

python pacman.py -l medium_maze -p SearchAgent

python pacman.py -l big_maze -z .5 -p SearchAgent

The Pacman board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). Is the exploration order what you would have expected? Does Pacman actually go to all the explored squares on his way to the goal?

Hint: If you use a Stack as your data structure, the solution found by your DFS algorithm for medium_maze should have a length of 130 (provided you push successors onto the fringe in the order provided by get_successors; you might get 246 if you push them in the reverse order). Is this a least cost solution? If not, think about what depth-first search is doing wrong.
Question 2 (10 points): Breadth First Search

Implement the breadth-first search (BFS) algorithm in the breadth_first_search function in search.py. Again, write a graph search algorithm that avoids expanding any already visited states. Test your code the same way you did for depth-first search.

python pacman.py -l medium_maze -p SearchAgent -a fn=bfs

python pacman.py -l big_maze -p SearchAgent -a fn=bfs -z .5

Does BFS find a least cost solution? If not, check your implementation.

Hint: If Pacman moves too slowly for you, try the option --frame_time 0.

Note: If you've written your search code generically, your code should work equally well for the eight-puzzle search problem without any changes.

python eight_puzzle.py

Question 3 (10 points): Varying the Cost Function

While BFS will find a fewest-actions path to the goal, we might want to find paths that are "best" in other senses. Consider medium_dotted_maze and medium_scary_maze.

By changing the cost function, we can encourage Pacman to find different paths. For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas, and a rational Pacman agent should adjust its behavior in response.

Implement the uniform-cost graph search algorithm in the uniform_cost_search function in search.py. We encourage you to look through util.py for some data structures that may be useful in your implementation. You should now observe successful behavior in all three of the following layouts, where the agents below are all UCS agents that differ only in the cost function they use (the agents and cost functions are written for you):

python pacman.py -l medium_maze -p SearchAgent -a fn=ucs

python pacman.py -l medium_dotted_maze -p StayEastSearchAgent

python pacman.py -l medium_scary_maze -p StayWestSearchAgent

Note: You should get very low and very high path costs for the StayEastSearchAgent and StayWestSearchAgent respectively, due to their exponential cost functions (see search_agents.py for details).
Question 4 (12 points): A* search

Implement A* graph search in the empty function a_star_search in search.py. A* takes a heuristic function as an argument. Heuristics take two arguments: a state in the search problem (the main argument), and the problem itself (for reference information). The null_heuristic heuristic function in search.py is a trivial example.

You can test your A* implementation on the original problem of finding a path through a maze to a fixed position using the Manhattan distance heuristic (implemented already as manhattan_heuristic in search_agents.py).

python pacman.py -l big_maze -z .5 -p SearchAgent -a fn=a_star,heuristic=manhattan_heuristic

You should see that A* finds the optimal solution slightly faster than uniform cost search (about 549 vs. 620 search nodes expanded in my implementation, but ties in priority may make your numbers differ slightly). What happens on open_maze for the various search strategies?
Question 5 (12 points): Finding All the Corners

The real power of A* will only be apparent with a more challenging search problem. Now, it's time to formulate a new problem and design a heuristic for it.

In corner mazes, there are four dots, one in each corner. Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not). Note that for some mazes like tiny_corners, the shortest path does not always go to the closest food first! Hint: the shortest path through tiny_corners takes 28 steps.

Note: Make sure to complete Question 2 before working on Question 5, because Question 5 builds upon your answer for Question 2.

Implement the CornersProblem search problem in search_agents.py. You will need to choose a state representation that encodes all the information necessary to detect whether all four corners have been reached. Now, your search agent should solve:

python pacman.py -l tiny_corners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l medium_corners -p SearchAgent -a fn=bfs,prob=CornersProblem

To receive full credit, you need to define an abstract state representation that does not encode irrelevant information (like the position of ghosts, where extra food is, etc.). In particular, do not use a Pacman GameState as a search state. Your code will be very, very slow if you do (and also wrong).

My implementation of breadth_first_search expands just under 2000 search nodes on medium_corners. However, heuristics (used with A* search) can reduce the amount of searching required.
Question 6 (12 points): Corners Problem: Heuristic

Note: Make sure to complete Question 4 before working on Question 6, because Question 6 builds upon your answer for Question 4.

Implement a non-trivial, consistent heuristic for the CornersProblem in corners_heuristic in search_agents.py.

python pacman.py -l medium_corners -p AStarCornersAgent -z 0.5

Note: AStarCornersAgent is a shortcut for

-p SearchAgent -a fn=a_star_search,prob=CornersProblem,heuristic=corners_heuristic

Admissibility vs. Consistency: Remember, heuristics are just functions that take search states and return numbers that estimate the cost to a nearest goal. More effective heuristics will return values closer to the actual goal costs. To be admissible, the heuristic values must be lower bounded on the actual shortest path cost to the nearest goal (and non-negative). To be consistent, it must additionally hold that if an action has cost c, then taking that action can only cause a drop in heuristic of at most c.

Remember that admissibility isn't enough to guarantee correctness in graph search -- you need the stronger condition of consistency. However, admissible heuristics are usually also consistent, especially if they are derived from problem relaxations. Therefore it is usually easiest to start out by brainstorming admissible heuristics. Once you have an admissible heuristic that works well, you can check whether it is indeed consistent, too. The only way to guarantee consistency is with a proof. However, inconsistency can often be detected by verifying that for each node you expand, its successor nodes are equal or higher in in f-value. Moreover, if UCS and A* ever return paths of different lengths, your heuristic is inconsistent. This stuff is tricky!

Non-Trivial Heuristics: The trivial heuristics are the ones that return zero everywhere (UCS) and the heuristic which computes the true completion cost. The former won't save you any time, while the latter will timeout the autograder. You want a heuristic which reduces total compute time, though for this assignment the autograder will only check node counts (aside from enforcing a reasonable time limit).

Grading: Your heuristic must be a non-trivial non-negative consistent heuristic to receive any points. Make sure that your heuristic returns 0 at every goal state and never returns a negative value. Depending on how few nodes your heuristic expands, you'll be graded:
Number of nodes expanded 	Grade
more than 2000 	0/12
at most 2000 	4/12
at most 1600 	8/12
at most 1200 	12/12

 

Remember: If your heuristic is inconsistent, you will receive no credit, so be careful!
Question 7 (12 points): Eating All The Dots

Now we'll solve a hard search problem: eating all the Pacman food in as few steps as possible. For this, we'll need a new search problem definition which formalizes the food-clearing problem: FoodSearchProblem in search_agents.py (implemented for you). A solution is defined to be a path that collects all of the food in the Pacman world. For the present assignment, solutions do not take into account any ghosts or power pellets; solutions only depend on the placement of walls, regular food and Pacman. (Of course ghosts can ruin the execution of a solution! We'll get to that in the next programming assignment.) If you have written your general search methods correctly, A* with a null heuristic (equivalent to uniform-cost search) should quickly find an optimal solution to test_search with no code change on your part (total cost of 7).

python pacman.py -l test_search -p AStarFoodSearchAgent

Note: -p AStarFoodSearchAgent is a shortcut for -p SearchAgent -a fn=a_star,prob=FoodSearchProblem,heuristic=food_heuristic

You should find that UCS starts to slow down even for the seemingly simple tiny_search. As a reference, my implementation takes 2.5 seconds to find a path of length 27 after expanding 5057 search nodes.

Note: Make sure to complete Question 4 before working on Question 7, because Question 7 builds upon your answer for Question 4.

Fill in food_heuristic in search_agents.py with a consistent heuristic for the FoodSearchProblem. Try your agent on the tricky_search board:

python pacman.py -l tricky_search -p AStarFoodSearchAgent

My UCS agent finds the optimal solution in about 13 seconds, exploring over 16,000 nodes.

Any non-trivial non-negative consistent heuristic will receive 3 points. Make sure that your heuristic returns 0 at every goal state and never returns a negative value. Depending on how few nodes your heuristic expands, you'll get additional points:
Number of nodes expanded 	Grade
more than 15000 	3/12
at most 15000 	6/12
at most 12000 	9/12
at most 9000 	12/12 (full credit; medium)
at most 7000 	15/12 (optional extra credit; hard)

 

Remember: If your heuristic is inconsistent, you will receive no credit, so be careful! Can you solve medium_search in a short time? If so, I'm either very, very impressed, or your heuristic is inconsistent.
Question 8 (3 points): Suboptimal Search

Sometimes, even with A* and a good heuristic, finding the optimal path through all the dots is hard. In these cases, we'd still like to find a reasonably good path, quickly. In this section, you'll write an agent that always greedily eats the closest dot. ClosestDotSearchAgent is implemented for you in search_agents.py, but it's missing a key function that finds a path to the closest dot.

Implement the function find_path_to_closest_dot in search_agents.py. My agent solves this maze (suboptimally!) in under a second with a path cost of 350:

python pacman.py -l big_search -p ClosestDotSearchAgent -z .5 

Hint: The quickest way to complete find_path_to_closest_dot is to fill in the AnyFoodSearchProblem, which is missing its goal test. Then, solve that problem with an appropriate search function. The solution should be very short!

Your ClosestDotSearchAgent won't always find the shortest possible path through the maze. Make sure you understand why and try to come up with a small example where repeatedly going to the closest dot does not result in finding the shortest path for eating all the dots.
Coding Standard / Linter

Remember:

    All code is expected to follow the PEP8 Links to an external site.style guide and PEP257 Links to an external site.docstring conventions.
    All modified files must include your header + statement of authenticity (see Header and Authenticity Statement).  This should go in the module level docstring above the existing header/license information.  Failure to include this may result in an automatic 0!

In order to help verify you are following these criteria the autograder will use a linter Links to an external site. + additional checks to analyze your code (note: this only runs when autograding the whole assignment, not a specific question/test; or you can run the autograder with the --just_lint option to just run the linter).  Specifically it uses flake8 Links to an external site. with the pep8-naming Links to an external site. and flake8-docstrings Links to an external site. plugins.  If you do not have these installed the autograder will instruct you to do so by running:

pip install flake8 pep8-naming flake8-docstrings

Important: while this code analysis has been incorporated into the autograder to help you be sure you are writing compliant code, it will be my ultimate judgment not the linter's that will determine your grade.
Submission

When you have completed all questions, you should create a zip file containing just search.py and search_agents.py and upload this to canvas! Remember: if you work as a group, be sure to put all names in the file headers, and each member still needs to submit
Grading

This assignment will be graded out of 100 points.

All questions are worth the value described above + submitting as directed and following PEP8 Links to an external site.style and PEP257 Links to an external site.docstring conventions is worth 10 points.

 

 

 
Attribution

Champlain College CSI-480, Fall 2018
This assignment was adapted by Joshua Auerbach (jauerbach@champlain.edu)
from the UC Berkeley Pacman Projects: http://ai.berkeley.edu (Links to an external site.)Links to an external site.
These materials are freely available for educational use, as long as proper attribution is retained.
