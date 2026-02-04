squares=[x*x for x in range(10)]
print(squares)

squares_dict={x*x for x in range(10)}
print(squares_dict)

'''uniques_value={f(x) for x in data}
print(uniques_value)'''

'''lst =[x*x for x in range(10**6)]
print(lst)
gen =(x*x for x in range(10**6))
print(gen)'''

'''results=[]
for x in range(1_000_000):
    results.append(x*x )
print(results)'''

import numpy as np
arr =np.arange(10)
results=arr*arr
print(results)