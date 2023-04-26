import numpy as np
import random as rn
import matplotlib.pyplot as plt

class Walk:
    def __init__( self ):
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )
        self.y = np.array( [ 0 ] )
        self.returns = np.array( [ 0 ] )

    def step( self ):
        p = rn.random()
        if p < 0.25:
            self.x = np.append( self.x, self.x[ -1 ] - 1 )
            self.y = np.append( self.y, self.y[ -1 ] )
        elif p < 0.50:
            self.x = np.append( self.x, self.x[ -1 ] + 1 )
            self.y = np.append( self.y, self.y[ -1 ] )
        elif p < 0.75:
            self.x = np.append( self.x, self.x[ -1 ] )
            self.y = np.append( self.y, self.y[ -1 ] - 1 )
        else:
            self.x = np.append( self.x, self.x[ -1 ] )
            self.y = np.append( self.y, self.y[ -1 ] + 1 )
        self.t = np.append( self.t, self.t[ -1 ] + 1 )

        if self.x[ -1 ] == 0 and self.y[ -1 ] == 0:
            self.returns = np.append( self.returns, self.t[-1] )

w = Walk()
iter = 1e3

for i in range( int(iter) ):
    w.step()

print( 'Returned', w.returns.shape[ 0 ] - 1, 'times' )
print( 'Return times:', w.returns )

#uncomment to see a plot of the walk
'''
plt.plot( w.x, w.y, 'bo-' )
plt.plot( 0, 0, 'ro' )
plt.show()
'''
