def stat_rolls():
    import numpy as np
    rolls = np.sort(np.random.randint(1,7, size=(6,4))) 
    best_rolls = rolls[:,1:] 
    scores = np.sum(best_rolls, axis=1) 
    return(scores)
