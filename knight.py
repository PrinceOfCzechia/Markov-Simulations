import numpy as np
import random as rn

class Board:
    def __init__( self ):
        self.board = np.zeros( ( 8, 8 ) )

    def print( self ):
        print( self.board )

    def add( self, row, col ):
        self.board[row, col] += 1

def contrast( benchmark: Board, another: Board ):
    result = Board()
    for i in range( 8 ):
        for j in range( 8 ):
            result.board[ i ][ j ] = np.round( another.board[ i ][ j ] / benchmark.board[ i ][ j ], 2 )
    return result



class Knight():
    def __init__( self, row, col, board: Board ):
        self.position = np.array( [ row, col ] )
        self.board = board

    def generate_move( self ):
        r = rn.random()
        if r < 0.125: return np.array( [ -2, 1 ] )
        elif r < 0.250: return np.array( [ -2, -1 ] )
        elif r < 0.375: return np.array( [ -1, 2 ] )
        elif r < 0.500: return np.array( [ -1, -2 ] )
        elif r < 0.625: return np.array( [ 1, 2 ] )
        elif r < 0.750: return np.array( [ 1, -2 ] )
        elif r < 0.875: return np.array( [ 2, 1 ] )
        else: return np.array( [ 2, -1 ] )

    def check_move( self ):
        global candidate
        candidate = self.generate_move()
        if self.position[ 0 ] + candidate[ 0 ] >= 0 and \
           self.position[ 0 ] + candidate[ 0 ] < 8 and \
           self.position[ 1 ] + candidate[ 1 ] >= 0 and \
           self.position[ 1 ] + candidate[ 1 ] < 8 :
            return True
        else: return False

    def execute_move( self ):
        while not self.check_move():
            self.check_move()
        self.position += candidate
        self.board.add( self.position[ 0 ], self.position[ 1 ] )


b = Board()
k = Knight( 4, 4, b )
iter = 1e5

for i in range( int(iter) ):
    k.execute_move()

aux = [
       [ 2, 3, 4, 4, 4, 4, 3, 2 ],
       [ 3, 4, 6, 6, 6, 6, 4, 3 ],
       [ 4, 6, 8, 8, 8, 8, 6, 4 ],
       [ 4, 6, 8, 8, 8, 8, 6, 4 ],
       [ 4, 6, 8, 8, 8, 8, 6, 4 ],
       [ 4, 6, 8, 8, 8, 8, 6, 4 ],
       [ 3, 4, 6, 6, 6, 6, 4, 3 ],
       [ 2, 3, 4, 4, 4, 4, 3, 2 ]
      ]

theoretical = Board()
for i in range( 8 ):
    for j in range( 8 ):
        theoretical.board[ i ][ j ] = np.round( aux[ i ][ j ] / 336 * iter, 0 )

print( 'Empirical:')
k.board.print()
print( 'Theoretical:')
theoretical.print()
print( 'Comparison (Theoretical as a benchmark):')
contrast( theoretical, k.board ).print()
