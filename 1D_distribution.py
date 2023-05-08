import numpy as np
import random as rn 
import matplotlib.pyplot as plt

class Walk:
    def __init__( self ):
        self.position = 0
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )

    def step( self ):
        p = rn.random()
        if p < 0.5: self.position -= 1
        else: self.position += 1
        self.t = np.append( self.t, self.t[ -1 ] + 1 )
        self.x = np.append( self.x, self.position )

    def reinit( self ):
        self.position = 0
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )

w = Walk()

walk_count = 1e3
iter = 50
histogram = np.zeros( 2*iter + 1 )

for j in range( int(walk_count) ):
    for i in range( int(iter) ):
        w.step()
        histogram[ w.x[-1] + iter ] += 1
    w.reinit()

print( histogram )
plt.bar( np.linspace( -iter, iter, 2*iter + 1), histogram, width = 1, color = 'green' )
plt.show()
