import numpy as np
import sys

t = [[0,1,0,0,0], [0,0,0.5,0.5,0], [0,0,0,1,0], [0.5,0,0,0,0.5], [0,0,1,0,0]]
t_prev = [0.2, 0.2, 0.2, 0.2, 0.2]
alpha = 0.2
trans_mat = np.array(t)

num_rows, num_cols = trans_mat.shape

s = np.ones((num_cols, num_cols))
s_mat = np.matrix(s)
trans_mat_new = (1.0 - alpha) * trans_mat + alpha/num_cols * s_mat
trans_arr_new = np.array(trans_mat_new)
print('Transition matrix after using teleportation factor is\n')
print(trans_mat_new)
print('\n')

num_iter = 0
while True:
    num_iter = num_iter + 1
    print('Iteration : ', num_iter, ' ', t_prev)
    t_curr = []
    for col in range(trans_arr_new.shape[1]):
        product = np.dot(trans_arr_new[:, col], t_prev)
        t_curr.append(product)
    
    max_diff = -sys.maxsize - 1
    for j in range(len(t_curr)):
        diff = abs(t_curr[j] - t_prev[j])
        if diff > max_diff:
            max_diff = diff
    
    t_prev = t_curr
    if(max_diff <= 0.0001):
        break

print('\nNumber of iterations are')
print(num_iter)