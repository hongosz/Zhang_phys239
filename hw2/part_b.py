import numpy as np 
pc = (3.086 *10**17)    #[cm] 
D = (100 * pc )
n = 1.                   #[cm^-3]

def calcI(sig,I0,S):
    ds = 100                         #Define the number of steps 
    Dist = np.linspace(0, D, ds)     #Produce the evenly spaced distance vector 
    I = np.zeros(ds)                 #Initialize specific intensity vector 
    I[0] = I0     
    
    #Populate the specific intensity vectory by calculating the change at every step ds 
    
    for i in np.arange(1,ds):
        I[i] = I[i-1]+ (S - I[i-1])*((Dist[i]-Dist[i-1])*n*sig)
    return I[ds-1] 
