# **Forest Fire Propagation Model**

## Descriptioon
This is a Python program that simulates the propagation of a forest fire. The program uses a two-dimensional dictionary to represent the forest, where each key is a tuple of x and y coordinates, and the value is either a tree ('🌲'), fire ('🔥'), or an empty space (' '). The simulation works by growing trees randomly, and then setting them on fire with a certain probability. If a tree catches fire, the fire spreads to its neighboring trees until it burns down.

## Requirements
Python 3 and the bext library are required for this application, which can be installed with pip: pip install 'bext'

## Constants
The program has several constants that can be adjusted to change the behavior of the simulation:
1.	WIDTH and HEIGHT: The size of the forest.
2.	TREE, FIRE, and EMPTY: Characters used to represent trees, fire, and empty spaces in the forest.
3.	INITIAL_TREE_DENSITY: The amount of forest that starts with a tree.
4.	GROW_CHANCE: The chance that an empty space turns into a tree in each simulation step.
5.	FIRE_CHANCE: The chance that a tree is hit by lightning and catches fire in each simulation step.
6.	PAUSE_LENGTH: The amount of time (in seconds) to pause between simulation steps.

### Functions
The program has three main functions:
1.	main(): The main program loop. It creates a new forest, and then runs the simulation until the program is interrupted.
2.	create_new_forest(): Creates a new forest data structure, with a certain initial tree density.
3.	display_forest(forest): Displays the forest on the screen using colored text.

## Running the Program
Just launch the forest fire.py file to get started.
Ctrl-C will close the application.
