import numpy as np
import random as rn

class Walk:
    def __init__( self ):
        self.x = np.array( [ 0 ] )
        self.y = np.array( [ 0 ] )
        self.z = np.array( [ 0 ] )

    def reinit( self ):
        self.x = np.array( [ 0 ] )
        self.y = np.array( [ 0 ] )
        self.z = np.array( [ 0 ] )

    def step( self, x, y, z ):
        self.x = np.append( self.x, self.x[ -1 ] + x )
        self.y = np.append( self.y, self.y[ -1 ] + y )
        self.z = np.append( self.y, self.y[ -1 ] + z )

    def eval( self ):
        p = rn.random()
        if p < 1/6:
            self.step( -1, 0, 0 )
        elif p < 2/6:
            self.step( 1, 0, 0 )
        elif p < 3/6:
            self.step( 0, -1, 0 )
        elif p < 4/6:
            self.step( 0, 1, 0 )
        elif p < 5/6:
            self.step( 0, 0, -1 )
        else:
            self.step( 0, 0, 1 )

num_returns = 0
walk_count = 1e5
iter = 1e2

w = Walk()

for i in range( int(walk_count) ):
    w.reinit()
    for i in range( int(iter) ):
        w.eval()
        if w.x[-1] == 0 and w.y[-1] == 0 and w.z[-1] == 0:
            num_returns += 1
            break

print( num_returns, 'out of', walk_count, 'returned' )
print( 'Return probability p =', np.round( num_returns / walk_count, 3 ) )
