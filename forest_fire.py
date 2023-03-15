# Forest Fire Propagation Model.


import random
import sys
import time
import bext

# Set up constants.
WIDTH = 80
HEIGHT = 25

TREE = ' 🌲 '
FIRE = '🔥'
EMPTY = ' '

INITIAL_TREE_DENSITY = 0.10  # Amount of forest that starts with fire.
GROW_CHANCE = 0.02  # Chance a blank space turns into tree.
FIRE_CHANCE = 0.10  # Chance a tree is hit by lightning and burns.

PAUSE_LENGTH = 0.5


def main():
    forest = create_new_forest()
    bext.clear()

    while True:  # Main program loop.
        display_forest(forest)

        # Run a single simulation step:
        next_forest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in next_forest:
                    continue

                if ((forest[(x, y)] == EMPTY) and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    next_forest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE) and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    next_forest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning, Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):

                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                next_forest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    next_forest[(x, y)] = EMPTY
                else:
                    next_forest[(x, y)] = forest[(x, y)]
        forest = next_forest

        time.sleep(PAUSE_LENGTH)


def create_new_forest():
    # Returns a dictionary for a new forest data structure.
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def display_forest(forest):
    # Display the forest data structure on the screen.
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')

        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}% '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}% '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
