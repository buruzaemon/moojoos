import numpy as np

def diff_of_diff(arr, idx, off=2):  
    """
    No-reference blur estimation based on Sharpness Estimation for Document
    and Scene Images (Kumar, Chen and Doermann). Returns the difference of 
    differences (DoM) for a single point of a row (col) in an image.

    Args:
        arr (list): list of values corresponding to a row (col) in an image
        idx (int): index of array item to examine
        off (int): positive integer for calculating index range for DoM

    Returns:
        dom (int): the difference of differences for a single image point

    Raises:
        IndexError
    
    """
    if idx < 0 or idx > len(arr)-1:
        raise IndexError("index %d is out of bounds for array of length %d" % (idx, len(arr)))
              
    diff_u = arr[-1]-arr[idx] if (idx >= len(arr)-off) else arr[idx+off]-arr[idx]
    diff_l = arr[idx]-arr[0]  if (idx < off) else arr[idx]-arr[idx-off] 

    return np.abs(diff_u - diff_l)
