import numpy as np 
import random as rn

class Walk:
    def __init__( self ):
        self.x = np.zeros( 1 )
        self.y = np.zeros( 1 )
        self.z = np.zeros( 1 )
        self.u = np.zeros( 1 )

    def reinit( self ):
        self.x = np.zeros( 1 )
        self.y = np.zeros( 1 )
        self.z = np.zeros( 1 )
        self.u = np.zeros( 1 )

    def step( self, x, y, z, u ):
        self.x = np.append( self.x, self.x[ -1 ] + x )
        self.y = np.append( self.y, self.y[ -1 ] + y )
        self.z = np.append( self.z, self.z[ -1 ] + z )
        self.u = np.append( self.u, self.u[ -1 ] + u )

    def eval( self ):
        p = rn.random()
        if p < 1/8:
            self.step( -1, 0, 0, 0 )
        elif p < 2/8:
            self.step( 1, 0, 0, 0 )
        elif p < 3/8:
            self.step( 0, -1, 0, 0 )
        elif p < 4/8:
            self.step( 0, 1, 0, 0 )
        elif p < 5/8:
            self.step( 0, 0, -1, 0 )
        elif p < 6/8:
            self.step( 0, 0, 1, 0 )
        elif p < 7/8:
            self.step( 0, 0, 0, -1 )
        else:
            self.step( 0, 0, 0, 1 )

num_returns = 0
walk_count = 1e3
iter = 1e3

w = Walk()

for i in range( int(walk_count) ):
    w.reinit()
    for i in range( int(iter) ):
        w.eval()
        if w.x[-1] == 0:
            if w.y[-1] == 0:
                if w.z[-1] == 0:
                    if w.u[-1] == 0:
                        num_returns += 1
                        break

print( num_returns, 'out of', walk_count, 'returned' )
print( 'Return probability p =', np.round( num_returns / walk_count, 3 ) )
