 import os
 from PIL import Image
 import numpy as np
 results_dir = 'results/'
 new_dir = 'results_dir/'
 images = os.listdir(results_dir)
 
 for img_path in images:
     im = Image.open(results_dir+img_path)
     im = np.array(im,dtype=np.uint8)
     l=[[0, 7], [1,8], [2,11], [3,12], [4,13], [5,17], [6,19], [7,20], [8,21], [9,22], [10,23], [11,24], [12,25], [13,26], [14,27],
     [15,28], [16,31], [17,32], [18,33]]
 
     out_np_new=np.zeros_like(im)  #initialize with unlabeld
     for i in l:
         out_np_new[im==i[0]]=i[1]
 
     Image.fromarray(out_np_new).save(new_dir+img_path,'PNG')
