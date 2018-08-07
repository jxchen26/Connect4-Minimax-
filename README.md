# Intro

This a connect4 game with GUI made in python 3.6. The program consist of two game modes, first being player vs. player, and the second computer vs player. The computer player (AI) is implemented using an minimax algorithm, and a set of heuristics to evaluate each move and a given game state. The code will need pygame, numpy, math, amd sys libraries to run.    

# About the Program

The minimax alorigthm has a pratical search depth of 5, and the AI can play at a easy to moderate level. At search depth of 5, it takes about 5 to 7 seconds to compute a move (when there are still 7 columes available), while a search depth of 6 takes about 20 to 30 seconds to compute a move.

In addition, the current set of heuristics fails to account for "almost pointless moves" such as filling up a 3 in a row that leads to no where. This is due to the fact a score is not given to a move base on its surrounding empty slots.   
