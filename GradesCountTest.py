import numpy as np

result = np.random.randint(60,101,size=(5,4))
#随便设的，不忍心让别人挂科
print(f"他们的总分依次是{result.sum(axis=1)}")
print(f"每门课的平均分依次是{result.mean(axis=0)}")
max_index = np.argmax(result)
point = np.unravel_index(max_index,result.shape)
max_score = result[point]
print(f"最高分是{max_score},坐标是{point}")