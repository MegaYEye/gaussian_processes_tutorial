
#------------------------------------------------------------
# kernel
def sqrExpKernel1(a, b):
    n = len(a)
    K = np.zeros((n,n))
    for i in np.arange(n):
        for j in np.arange(n):
            K[i, j] = np.exp(-0.5*(a[i] - b[j])**2.0)
    return K
