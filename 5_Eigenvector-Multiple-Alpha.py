import numpy as np
import matplotlib.pyplot as plt

def get_new_transition_matrix(trans_mat, alpha):
    num_rows, num_cols = trans_mat.shape
    s = np.ones((num_cols, num_cols))
    s_mat = np.matrix(s)
    trans_mat_new = (1.0 - alpha) * trans_mat + alpha/num_cols * s_mat
    trans_arr_new = np.array(trans_mat_new)
    # print(trans_mat_new)
    return trans_arr_new

def get_page_rank(trans_arr_new):
    eigenvalues, eigenvectors = np.linalg.eig(trans_arr_new.T)
    ind = np.argmax(eigenvalues)
    largest = eigenvectors[:, ind]
    largest = largest.real
    largest = largest/largest.sum()
    # print(largest)
    return largest

t = [[0,1/3,1/3,1/3], [0,0,1/2,1/2],[1,0,0,0],[1/2,0,1/2,0]]
trans_mat = np.matrix(t)
alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in range(len(alpha)):
    trans_arr_new = get_new_transition_matrix(trans_mat, alpha[i])
    page_ranks = get_page_rank(trans_arr_new)
    print('alpha = ', alpha[i], ' PageRanks = ', page_ranks)
    # print(page_ranks)
    plt.scatter([alpha[i]] * len(page_ranks), page_ranks)
    for j in range(len(page_ranks)):
      plt.text(alpha[i], page_ranks[j], j+1, fontsize=12)

plt.xlabel('Teleportation factor (alpha)', fontweight ='bold')
plt.ylabel('PageRank values', fontweight ='bold')
plt.xticks(alpha)
plt.show()