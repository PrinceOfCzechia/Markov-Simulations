# Markov-Simulations
Numpy based simulations of Markov processes. Since the point is to demonstrate mathematical phenomena, the code does not look after the user very much. The author presumes everyone knows that probabilities are in \[ 0, 1 \] and what dimensions of vectors and matrices are multipliable.

### stationary.py
Simulates convergence of a Markov chain to its stationary distribution.

### drift.py
Simulates a random walk which drifts to `-inf`. The user chooses *p*, probability of moving towards `inf`, the code returns the highest state reached

![Example output of *drift.py*](img/drift.png)

### knight.py
Simulates a random walk of a knight on a chessboard.

![Example output of *knight.py*](img/knight.png)