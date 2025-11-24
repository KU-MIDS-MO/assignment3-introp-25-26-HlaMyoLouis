import numpy as np

def count_values_in_bins(data, bin_edges):
    data=np.array(data)
    bin_edges=np.array(bin_edges)
    
    B=len(bin_edges)-1
    counts=np.zeros(B, dtype=int)
            
    for i in range(B):
        left=bin_edges[i]
        right=bin_edges[i+1]
        if i < B-1:
            mask=(data >= left) & (data < right)
        else:
            mask=(data >= left) & (data <= right)
        counts[i]=np.sum(mask)
        
    return counts

