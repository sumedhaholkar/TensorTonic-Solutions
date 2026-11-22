import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    y=np.asarray(y,dtype=float)
    sum=0.0
    m=len(x)
    for i in range(0,m):
        sum=sum+(abs(x[i]-y[i]))
    return sum
    pass