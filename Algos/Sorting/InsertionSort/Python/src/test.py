import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

from insertionSort import *

start = time.time()
test_array = []
full_results = []

for i in range(1,200):
    start = time.time()
    for value in range(0, i):
        test_array.append(np.random.randint(1, 15))

    sorted_array = sort(test_array)
    full_results.append(time.time() - start)

df = pd.DataFrame({'Time (s)': full_results})

df.plot()
plt.show()

