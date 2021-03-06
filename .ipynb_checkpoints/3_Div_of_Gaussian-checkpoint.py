def Divergence(sigma,n=0): #dont give n as an input (n is for generate DoG)
    if n==0:
        n=int((4*sigma)%2==0)+4*sigma
    kernal=np.zeros((n,n))
    for i in range(-(n//2),n//2+1):
        for j in range(-(n//2),n//2+1):
            val=i*np.exp(-(i**2+j**2)/(2*sigma**2))+j*np.exp(-(i**2+j**2)/(2*sigma**2))
            kernal[i+n//2][j+n//2]=val
    return (kernal)