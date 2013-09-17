import numpy as np

def diffofdiff(arr, idx, off=2):  
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

def contrast(arr, idx, off=2):
    """
    Returns the contrast value for a given edge pixel in a row (col).
        
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
        C : integer
            Integer from 0 or greater, representing the contrast at an edge
            pixel. Used to normalize the DoM value to yield the sharpness
            measurement of an edge pixel.
            
            Contrast is defined as:
                
                C = Sum |I(k,j) - I(k-1,j)| 
                 
                    where, given idx, k ranges from idx-off to idx+off+1
    
    Raises
    ------
        IndexError    
    """
    if idx < 0 or idx > len(arr)-1:
        raise IndexError("index %d is out of bounds for array of length %d" % (idx, len(arr)))
        
    start = [ 0 if e < 0 else e for e in xrange(idx-off, idx+off+1)]
    end   = [ 0 if (e-1)<0 else (e-1) for e in start ]
    
    ii = zip(start, end)
    
    return np.sum([ np.abs( int(arr[e[0]]) - int(arr[e[1]]) ) for e in ii ])
    