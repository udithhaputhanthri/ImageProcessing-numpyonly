def conv2D(img,kernal):
    img_conv=np.zeros(np.array(img.shape))
    n=kernal.shape[0]
    for i in range(n//2,img.shape[0]-n//2):
        for j in range(n//2,img.shape[1]-n//2):
            pixel=0
            #print('image_point :',(i,j))
            for k in range(-(n//2),n//2+1):
                for m in range(-(n//2),n//2+1):
                    #print('neighbourhood :',(i+k,j+m))
                    #print(n//2+k,n//2+m)
                    pixel+=img[i+k][j+m]*kernal[n//2+k][n//2+m]
            img_conv[i][j]=pixel          
    return img_conv