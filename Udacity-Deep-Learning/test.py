
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    #    pass  # TODO: Compute and return softmax(x)
    return np.exp(x)/np.sum(np.exp(x),axis=0)
scores = np.array([3.0, 1.0, 0.2])

print(softmax(scores))
print(softmax(scores*10))
print(softmax(scores/10))