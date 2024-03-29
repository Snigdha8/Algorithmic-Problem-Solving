import numpy as np

t = [[0,1,0,0,0], [0,0,0.5,0.5,0], [0,0,0,1,0], [0.5,0,0,0,0.5], [0,0,1,0,0]]
trans_mat = np.matrix(t)
alpha = 0.2
num_rows, num_cols = trans_mat.shape
s = np.ones((num_cols, num_cols))
s_mat = np.matrix(s)
trans_mat_new = (1.0 - alpha) * trans_mat + alpha/num_cols * s_mat
trans_arr_new = np.array(trans_mat_new)


eigenvalues, eigenvectors = np.linalg.eig(trans_arr_new.T)
ind = np.argmax(eigenvalues)
largest = eigenvectors[:, ind]
largest = largest.real
largest = largest/largest.sum()
print(largest)