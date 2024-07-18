import random
import numpy as np

a = np.empty((0, 1), dtype=int)
for i in range(100):  
    value = random.randint(0, 99)  
    while value in a:  
        value = random.randint(0, 99)  
    a = np.append(a, [value])  
print(a)

prisoners_saved = 0
total_iterations = 0
for i in range(100):
    value = i  
    iterations = 0
    for j in range(50):  
        iterations += 1
        if a[value] == i:  
            prisoners_saved += 1  
            break  
        else:
            value = a[value]  
    total_iterations += iterations
    print(f"Prisoner {i} escaped in {iterations} iterations")
print(f"Prisoners saved: {prisoners_saved}")
print(f"Total iterations: {total_iterations}")
print(f"Average iterations per prisoner: {total_iterations / 100}")