# Make image (as a matrix) that tiles multiple smaller matrices (images) in 2d
# In Matlab, this is called the "montage" function.
# Source 
#http://www.datawrangling.org/python-montage-code-for-displaying-arrays/
  
from numpy import array,flipud,shape,zeros,rot90,ceil,floor,sqrt
import pylab
 
def montage(X, colormap=pylab.cm.gist_gray):    
    m, n, count = shape(X)    
    mm = int(ceil(sqrt(count)))
    nn = mm
    M = zeros((mm * m, nn * n))

    image_id = 0
    for j in range(mm):
        for k in range(nn):
            if image_id >= count: 
                break
            sliceM, sliceN = j * m, k * n
            M[sliceN:sliceN + n, sliceM:sliceM + m] = X[:, :, image_id]
            image_id += 1
                    
    pylab.imshow(flipud(rot90(M)), cmap=colormap)
    pylab.axis('off')             