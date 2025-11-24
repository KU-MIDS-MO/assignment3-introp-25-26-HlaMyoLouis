import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
   scores = np.array(scores, dtype=float)
   scores[scores<min_score]=min_score
   scores[scores>max_score]=max_score
   scaled=(scores - min_score) / (max_score - min_score)
   return scaled
          
       
       
