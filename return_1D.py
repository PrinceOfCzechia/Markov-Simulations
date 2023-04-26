import numpy as np 
import random as rn
import matplotlib.pyplot as plt

class Walk:
    def __init__( self ):
        self.position = 0
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )
        self.returns = np.array( [ 0 ] )

    def step( self ):
        p = rn.random()
        if p < 0.5: self.position -= 1
        else: self.position += 1
        self.t = np.append( self.t, self.t[ -1 ] + 1 )
        self.x = np.append( self.x, self.position )
        if self.position == 0: self.returns = np.append( self.returns, self.t[-1] )

w = Walk()
iter = 1e2

for i in range( int(iter) ):
    w.step()

print( 'Returned', w.returns.shape[ 0 ] - 1, 'times' )
print( 'Return times:', w.returns )

#uncomment to see a plot of the walk

plt.step( w.t, w.x, 'b-' )
for val in w.returns:
    plt.plot( val, 0, 'ro' )
    plt.text( val, 0, str(val), horizontalalignment = 'center',
              fontweight = 'demi', fontstretch = 'ultra-condensed' )
plt.show()

