import numpy as np

def moving_average(signal, window_size):
   signal = np.asarray(signal)
   n = signal.size
    
   if n == 0:
      return np.array([], dtype=float)

   k = (window_size - 1)//2

   result = np.zeros(n, dtype=float)

   for i in range(n):
        left = max(0, i - k)
        right = min(n - 1, i + k)
        window = signal[left:right+1]
        result[i] = np.mean(window)

   return result
