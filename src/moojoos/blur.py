import numpy as np

def sharpness(arr, idx, width, off=2):
    if width < 1:
        raise ValueError("Width value of %d is illegal, must be greater than 0" % idx)
        
    ii = ( e for e in np.arange(idx-width, idx+width+1) )
    sum_dom, sum_c = 0, 0
    for i in ii:
        if i < 0:
            i = 0
        elif i >= len(arr):
            i = len(arr)-1
                
        sum_dom += _diffofdiff(arr, i, off)
        sum_c   += _contrast(arr, i)
    
    if sum_c == 0:
        sum_c = 0.0001 # avoid division by zero!
     
    return sum_dom/np.float(sum_c)
    

def _diffofdiff(arr, idx, off=2):  
    """
    Returns the difference of differences (DoM) for a single point of a row
    (col) of an image.
    
    No-reference blur estimation based on Sharpness Estimation for Document
    and Scene Images (Kumar, Chen and Doermann). 

    Parameters
    ----------
        arr : list
            List of values corresponding to a row (col) in an image
        idx : integer
            Index of array item to examine
        off : positive integer, optional
            Used to set upper and lower bounds for calculating the difference
            between the difference between upper bound and idx; and the
            difference between idx and lower bound
            
    Returns
    -------
        DoM : integer
            Integer from 0 or greater, representing the rate of slope change in
            a given range surrounding a specified point in an image.
        
            This is calculated via a difference of differences, DoM such that:
                
                DoM(i,j) = [I(i+off,j) - I(i,j)] - [I(i,j) - I(i-off,j)]
            
            This change in slope DoM is a discrete analog of the second 
            derivative for an image edge at the specified point (i,j).

    Raises
    ------
        IndexError
    
    """
    if idx < 0 or idx > len(arr)-1:
        raise IndexError("index %d is out of bounds for array of length %d" % (idx, len(arr)))
        
    a = arr.astype(int, copy=False)
        
    diff_u = a[-1]-arr[idx] if (idx >= len(a)-off) else a[idx+off]-a[idx]
    diff_l = a[idx]-arr[0]  if (idx < off) else a[idx]-a[idx-off]

    return np.abs(diff_u-diff_l)

def _contrast(arr, idx):
    """
    Returns the contrast value for a given edge pixel in a row (col).
        
    Parameters
    ----------
        arr : list
            List of values corresponding to a row (col) in an image
        idx : integer
            Index of array item to examine

    Returns
    -------
        C : integer
            Integer from 0 or greater, representing the contrast at an edge
            pixel. Used to normalize the DoM value to yield the sharpness
            measurement of an edge pixel.
            
            Contrast is defined as:
                
                C = Sum |I(k,j) - I(k-1,j)| 
                 
                    where, given idx, k ranges from idx-w to idx+w+1
    
    Raises
    ------
        IndexError    
    """
    if idx < 0 or idx > len(arr)-1:
       raise IndexError("index %d is out of bounds for array of length %d" % (idx, len(arr))) 

    if idx == 0:
        return 0
    else:
        return np.abs(int(arr[idx]) - int(arr[idx-1]))
    
#def _indexwindow(arr, idx, w=2):
#    if idx < 0 or idx > len(arr)-1:
#        raise IndexError("index %d is out of bounds for array of length %d" % (idx, len(arr)))
#        
#    start = [ 0 if e < 0 else e for e in xrange(idx-w, idx+w+1)]
#    end   = [ 0 if (e-1)<0 else (e-1) for e in start ]
#    
#    return zip(start, end)