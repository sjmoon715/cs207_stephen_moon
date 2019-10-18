import numpy as np
import pydoc

def L2(v, *args):
    """Compute the weighted L2 norm.
    
    INPUTS
    =======
    v: a list of numbers that represents a vector
    *args: optional, also a list that is interpreted as a vector of weights
    
    RETURNS
    ========
    L2 Norm: a floating point value for the L2 norm of the vector 

    NOTES
    =====
    PRE: 
        - Vector v must be given as a list of numbers
        - *args if provided must be a list of the same length as v
    POST:
        - Returns L2 Norm as a float
        - v and *args are not changed by the funtion

    EXAMPLES
    =========
    >>> L2([1,2,3])
    3.7416573867739413
    """
    
    
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)

