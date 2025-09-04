import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    # Defining the calculations in a loop for cleaner code
    calculations = {}
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
    for key, func in operations.items():
        calculations[key] = [
            func(arr, axis=0).tolist(),
            func(arr, axis=1).tolist(),
            func(arr).item()
        ]
    
    return calculations