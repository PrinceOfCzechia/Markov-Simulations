import random as rn
import numpy as np
from matplotlib import pyplot as plt

class Drift:
    def __init__( self, p ):
        # let 0 <= p < 1/2
        self.p = p
        self.S = 0
        self.M = 0
        self.num_positive = 0
        self.hist_y = np.zeros( 1200 )

    def step( self ):
        r = rn.random() # 0 <= r < 1
        if r < self.p:
            self.S += 1 # step towards +infty with probability p
            self.num_positive += 1
        else: self.S += -1 # step towards -infty with probability 1-p
        if self.S > self.M: self.M = self.S
        self.hist_y[ self.S + 1000 ] += 1

global_hist_y = np.zeros( 1200 )
avg_M = 0
max_M = 0
avg_num_positive = 0

iter = 1e3 # max reasonable value is 1e4
threshold = -1000
for i in range( int(iter) ):
    drift = Drift( 0.45 )
    while drift.S > threshold:
        drift.step()

    avg_M += drift.M
    avg_num_positive += drift.num_positive
    if drift.M > max_M: max_M = drift.M
    global_hist_y += drift.hist_y

theoretical_M = drift.p / ( 1 - 2 * drift.p) # p / ( q - p )

avg_M /= iter
avg_num_positive /= iter
print( '\nAverage empirical value of M after', int(iter), 'runs:', avg_M )
print( 'Theoretical M =', round( theoretical_M, 4 ) )
print( 'Highest M among all the walks:', max_M )
print( 'Average number of positive steps before reaching S =', threshold,':', avg_num_positive, '\n' )

#uncomment for plots
'''
plt.step( np.linspace( -1000, 200, 1200 ), global_hist_y )
plt.show()
'''