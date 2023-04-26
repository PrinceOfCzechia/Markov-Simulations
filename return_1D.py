import numpy as np 
import random as rn
import matplotlib.pyplot as plt

class Walk:
    def __init__( self ):
        self.position = 0
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )
        self.returns = np.empty( (1,1), dtype = int )

    def step( self ):
        p = rn.random()
        if p < 0.5: self.position -= 1
        else: self.position += 1
        self.t = np.append( self.t, self.t[ -1 ] + 1 )
        self.x = np.append( self.x, self.position )
        if self.position == 0: self.returns = np.append( self.returns, self.t[-1] )

w = Walk()
iter = 1e3

for i in range( int(iter) ):
    w.step()

print( 'Returned', w.returns.shape[ 0 ], 'times' )
print( 'Return times:', w.returns )

#uncomment for cool plots
'''
plt.plot( w.t, w.x, 'bo-' )
plt.show()
'''
