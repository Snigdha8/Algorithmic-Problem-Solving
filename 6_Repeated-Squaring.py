import numpy as np
import sys

modulo = 1000000007

def repeated_squaring(trans_mat, power):
    if(power == 0):
        return 1
    if(power == 1):
        # return trans_mat % modulo
        return trans_mat
    
    temp = repeated_squaring(trans_mat, int(power/2))
    # temp = np.dot(temp, temp) % modulo
    temp = np.dot(temp, temp)
    
    if(power % 2 == 0):
        return temp
    else:
        # return (np.dot(trans_mat % modulo, temp) % modulo)
        return (np.dot(trans_mat, temp))
        
        
t = [[0,1/3,1/3,1/3], [0,0,1/2,1/2],[1,0,0,0],[1/2,0,1/2,0]]
trans_mat = np.matrix(t)

t_prev = [0.25, 0.25, 0.25, 0.25]
t_prev_mat = np.matrix(t_prev)
exponent = 1
num_iter = 0
diff = -sys.maxsize - 1
while True:
    num_iter = num_iter + 1
    power = pow(2, exponent)
    temp_mat = repeated_squaring(trans_mat, power)
    t_curr = np.dot(temp_mat.T, t_prev_mat.T)
    print(t_curr.T)
    diff = np.subtract(t_prev_mat.T, t_curr).max()
    t_prev_mat = t_curr.T
    print(diff)
    if(diff <= 0.0001):
        break
    exponent = exponent + 1
    

print(num_iter)
