import numpy as np

results = np.random.randint(40,101,size=(5,4))

print(results.sum(axis=1))
print(results.mean(axis=0))

max = np.argmax(results)
point = np.unravel_index(max,results.shape)

print(f"最高分是{max},坐标是{point}")