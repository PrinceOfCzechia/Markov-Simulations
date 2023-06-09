import numpy as np

# probability matrix P
P1 = [
     [ 0.2, 0.6, 0.2 ],
     [ 0.3, 0.1, 0.6 ],
     [ 0.5, 0.0, 0.5 ] 
    ]

P_absorb = [
     [ 1/3, 1/3, 1/3 ],
     [ 0.0, 1/2, 1/2 ],
     [ 0.0, 0.0, 1.0 ]
    ]

P_rat = [
         [ 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 ],
         [ 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 ],
         [ 1/4, 1/4, 0.0, 1/4, 1/4, 0.0 ],
         [ 0.0, 0.0, 1/2, 0.0, 0.0, 1/2 ],
         [ 0.0, 0.0, 1/2, 0.0, 0.0, 1/2 ],
         [ 0.0, 0.0, 0.0, 1/2, 1/2, 0.0 ]
        ]

P_uphill = [
            [ 0.70, 0.30, 0.00, 0.00, 0.00, 0.00 ],
            [ 0.70, 0.00, 0.30, 0.00, 0.00, 0.00 ],
            [ 0.00, 0.70, 0.00, 0.30, 0.00, 0.00 ],
            [ 0.00, 0.00, 0.70, 0.00, 0.30, 0.00 ],
            [ 0.00, 0.00, 0.00, 0.70, 0.00, 0.30 ],
            [ 0.00, 0.00, 0.00, 0.00, 0.70, 0.30 ]
           ]

# initial state vector
s_ini = [ 0,0,0,0,0,1 ]

# try to reach a stationary state
aux = s_ini
for i in range(10000):
    s = np.dot(aux, P_uphill)
    if np.array_equal(s, aux):
        print('Stationary distribution', s, 'reached in iteration', i)
        break
    aux = s