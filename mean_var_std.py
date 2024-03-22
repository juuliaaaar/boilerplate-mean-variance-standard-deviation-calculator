import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)
    
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()]
    var = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()]
    std = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()]
    maxi = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist()]
    mini = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist()]
    summ = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
    
    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': maxi,
        'min': mini,
        'sum': summ
    }

    return calculations