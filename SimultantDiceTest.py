import numpy as np

results = np.random.randint(1,7,size=(1000))

value,counts = np.unique(results,return_counts=True)

print(counts)