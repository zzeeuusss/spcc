import random

def hill_climbing(initial_state):
    current_state = initial_state
    current_value = objective_function(current_state)
    
    for _ in range(1000):
        next_state = current_state + random.choice([-1, 1])
        next_value = objective_function(next_state)
        
        if next_value > current_value:
            current_state = next_state
            current_value = next_value
        else:
            break
    
    return current_state, current_value


def objective_function(x):
    return (x ** 2)  

initial_state = random.randint(-100, 100)
peak, value = hill_climbing(initial_state)
print(f"Peak found at x = {peak}, Value: {value}")
