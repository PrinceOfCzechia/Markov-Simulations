import random as rn

class Drift:
    def __init__( self, p ):
        # let 0 <= p < 1/2
        self.p = p
        self.S = 0
        self.M = 0
        self.num_positive = 0

    def step( self ):
        r = rn.random() # 0 <= r < 1
        if r < self.p:
            self.S += 1 # step towards +infty with probability p
            self.num_positive += 1
        else: self.S += -1 # step towards -infty with probability 1-p
        if self.S > self.M: self.M = self.S

    def reinit( self ):
        self.S = 0
        self.M = 0

avg_M = 0
max_M = 0
avg_num_positive = 0

iter = 1e4
threshold = -1000
for i in range( int(iter) ):
    walk = Drift( 0.45 )
    while walk.S > threshold:
        walk.step()

    avg_M += walk.M
    avg_num_positive += walk.num_positive
    if walk.M > max_M: max_M = walk.M

theoretical_M = walk.p / ( 1 - 2 * walk.p)

avg_M /= iter
avg_num_positive /= iter
print( 'Average empirical value of M after', int(iter), 'runs:', avg_M )
print( 'Theoretical M =', round( theoretical_M, 4 ) )
print( 'Highest M among all the walks:', max_M )
print( 'Average number of positive steps before reaching S =', threshold,':', avg_num_positive )