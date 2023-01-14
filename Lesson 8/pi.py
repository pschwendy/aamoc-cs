import random
import math

def calculate_pi(num_cycles: int) -> float:
    i = 0
    num_points_inside = 0
    while i < num_cycles:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        distance = math.sqrt(x**2 + y**2)
        if distance < 1:
            num_points_inside += 1
        
        i += 1
    
    return 4 * num_points_inside / num_cycles

print(f"With 100 cycles, pi is {calculate_pi(100)}")
print(f"With 1,000 cycles, pi is {calculate_pi(1000)}")
print(f"With 10,000 cycles, pi is {calculate_pi(10000)}")
print(f"With 100,000 cycles, pi is {calculate_pi(100000)}")
print(f"With 10,000,000 cycles, pi is {calculate_pi(10000000)}")