"""useful functions I wrote during bootcamp"""


def ECDF(data):
    """calculate cumulative distribution function of data"""
    
    x= np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x,y
