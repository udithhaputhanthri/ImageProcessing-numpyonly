def laplacian(sigma):
    n=2*(int(int(3*sigma+1)%2==0)+int(3*sigma+1))+1
    kernal=np.zeros((n,n))
    for i in range(-(n//2),n//2+1):
        for j in range(-(n//2),n//2+1):
            val=(i**2+j**2-2*sigma**2)*np.exp(-(i**2+j**2)/(2*sigma**2))
            kernal[i+n//2][j+n//2]=val
    return (kernal)/np.sum(kernal) 