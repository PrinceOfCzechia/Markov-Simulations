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
avg_num_positive = 0

walk = Drift( 0.49 )

iter = 1000000
threshold = -1000
for i in range( int(iter) ):
    while walk.S > threshold:
        walk.step()

    avg_M += walk.M
    avg_num_positive += walk.num_positive

avg_M /= iter
avg_num_positive /= iter
print( 'Average value of M after', iter, 'runs =', avg_M )
print( 'Average number of positive steps before reaching', threshold,'=', avg_num_positive )