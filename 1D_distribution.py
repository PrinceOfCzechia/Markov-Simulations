import numpy as np
import random as rn 
import matplotlib.pyplot as plt
from scipy.stats import variation

class Walk:
    def __init__( self ):
        self.position = 0
        self.t = np.array( [ 0 ] )
        self.x = np.array( [ 0 ] )
        self.max = 0
        self.abs_max = 0

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
        self.max = 0
        self.abs_max = 0

w = Walk()

walk_count = 1e3
iter = 50
h1 = np.zeros( 2*iter + 1 )
h_max = np.zeros( iter + 1 )
h_abs = np.zeros( iter + 1 )

for j in range( int(walk_count) ):
    for i in range( int(iter) ):
        w.step()
        h1[ w.x[-1] + iter ] += 1
    max = np.max( w.x )
    h_max[ max ] += 1
    abs = np.max( np.absolute( w.x ) )
    h_abs[ abs ] += 1
    w.reinit()

print( h1 )

f = plt.figure(1)
plt.figure( figsize = (8,3) )
plt.bar( np.linspace( -iter, iter, 2*iter + 1 ), h1, width = 1, color = 'purple' )
x = np.linspace( -iter, iter, 1000 )
sigma = variation( h1, ddof = 1 )
y = np.exp( -( x / (2*sigma) )**2 / 2 ) * np.max( h1 )
plt.plot( x, y, '--', color = 'green', linewidth = 0.8 )

g = plt.figure(2)
plt.figure( figsize = (8,3) )
plt.bar( np.linspace( 0, iter, iter + 1 ), h_max, width = 1, color = 'magenta' )

h = plt.figure(3)
plt.figure( figsize = (8,3) )
plt.bar( np.linspace( 0, iter, iter + 1 ), h_abs, width = 1, color = 'blue' )
plt.show()
