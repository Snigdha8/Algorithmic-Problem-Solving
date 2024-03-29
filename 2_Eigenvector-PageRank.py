import numpy as np

t = [[0,1,0,0,0], [0,0,0.5,0.5,0], [0,0,0,1,0], [0.5,0,0,0,0.5], [0,0,1,0,0]]
trans_mat = np.array(t)

eigenvalues, eigenvectors = np.linalg.eig(trans_mat.T)
ind = np.argmax(eigenvalues)
largest = eigenvectors[:, ind]
largest = largest.real
largest = largest/largest.sum() #Normalizing
print(largest)