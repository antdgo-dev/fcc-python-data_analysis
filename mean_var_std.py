# https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

# Public execution and test:
# https://replit.com/@ToniG4/boilerplate-mean-variance-standard-deviation-calculator


import numpy as np

def calculate(list) :

    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
    
    
    matrix3 = np.array(list).reshape(3, 3)


    calculations = {
        'mean' : [
            matrix3.mean(axis = 0).tolist(),
            matrix3.mean(axis = 1).tolist(),
            matrix3.mean()
        ],
        'variance' : [
            matrix3.var(axis = 0).tolist(),
            matrix3.var(axis = 1).tolist(),
            matrix3.var()
        ],
        'standard deviation' : [
            matrix3.std(axis = 0).tolist(),
            matrix3.std(axis = 1).tolist(),
            matrix3.std()
        ],
        'max' : [
            matrix3.max(axis = 0).tolist(),
            matrix3.max(axis = 1).tolist(),
            matrix3.max()
        ],
        'min' : [
            matrix3.min(axis = 0).tolist(),
            matrix3.min(axis = 1).tolist(),
            matrix3.min()
        ],
        'sum' : [
            matrix3.sum(axis = 0).tolist(),
            matrix3.sum(axis = 1).tolist(),
            matrix3.sum()
        ]
    }
    
    return calculations


print( calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]) )
