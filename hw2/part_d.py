import numpy as np 
import matplotlib.pyplot as plt

def calcI(sig,I0,S):
    ds = 100                         #Define the number of steps 
    Dist = np.linspace(0, D, ds)     #Produce the evenly spaced distance vector 
    I = np.zeros(ds)                 #Initialize specific intensity vector 
    I[0] = I0     
    
    #Populate the specific intensity vectory by calculating the change at every step ds 
    
    for i in np.arange(1,ds):
        I[i] = I[i-1]+ (S - I[i-1])*((Dist[i]-Dist[i-1])*n*sig)
    return I[ds-1] 
 
def gaussian(v,sig_0):
    return sig_0*np.exp(-np.power(v-50 , 2.) / (2 * np.power(5, 2.)))

v=np.linspace(0,100,100)       #Define a range of frequency 


pc = (3.086 *10**17)    #[cm] 
D = (100 * pc )
n = 1                   #[cm^-3]

#Using the definition of Column Density N = n*l 

N = (n*D)

#Using definition \tau = N \sigma_\nu 

sig_a = 10**(-3)/N  
sig_b = 1/N
sig_c = 10**3/N 



#We comment on one plot as an example as the rest of the plots follow in smiliar fashion. 
Iva = []                            #Initialize the specific intensity 
for i in gaussian(v,sig_b*8):
    Iva.append(calcI(i,9,8))        #Calculate Iv(D) for all frequencies in our range
Iva=np.array(Iva)
sa = np.ones(len(v))*8              #Define the source function array 
Iv0a = np.ones(len(v))*9            #Define the initial specific intensity array 

Ivb = []
for i in gaussian(v,sig_b):
    Ivb.append(calcI(i,9,5))
Ivb=np.array(Ivb)
sb = np.ones(len(v))*5
Iv0b = np.ones(len(v))*9

Ivc = []
for i in gaussian(v,sig_b/3):
    Ivc.append(calcI(i,0,5))
Ivc=np.array(Ivc)
sc = np.ones(len(v))*5
Iv0c = np.zeros(len(v))

#The differential equation approach don't work well under this limit.. We use the I ~ Iv(0)e^(-tau) + S(1-e^(-tau)) 
#result.
Ivd = np.ones(len(v))*5

Ive = []
for i in gaussian(v,sig_b/3):
    Ive.append(calcI(i,5,10))
Ive=np.array(Ive)
se = np.ones(len(v))*10
Iv0e = np.ones(len(v))*5

Ivf = []
for i in gaussian(v,sig_b*8):
    Ivf.append(calcI(i,5,10))
Ivf=np.array(Ivf)
sf = np.ones(len(v))*10
Iv0f = np.ones(len(v))*5


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10,3))
axes[0].plot(v,Iva,'k');
axes[0].plot(v,sa, 'k--');
axes[0].plot(v,Iv0a, 'k--');
axes[0].text(88, 8.1,'$S_{\\nu}$');
axes[0].text(88, 8.9,'$I_{\\nu}(0)$');
axes[0].set_title('case a');
axes[1].plot(v,Ivb,'k');
axes[1].plot(v,sb, 'k--');
axes[1].plot(v,Iv0b, 'k--');
axes[1].text(88, 5.4,'$S_{\\nu}$');
axes[1].text(88, 8.5,'$I_{\\nu}(0)$');
axes[1].set_title('case b');
axes[2].plot(v,Ivc,'k');
axes[2].plot(v,sc, 'k--');
axes[2].plot(v,Iv0c, 'k--');
axes[2].text(88, 4.6,'$S_{\\nu}$');
axes[2].text(88, 0.2,'$I_{\\nu}(0)$');
axes[2].set_title('case c');
fig, axes2 = plt.subplots(nrows=1, ncols=3, figsize=(10,3))
axes2[0].plot(v,Ivd,'k');
axes2[0].text(88, 5.1, '$S_{\\nu}$');
axes2[0].set_title('case d');
axes2[1].plot(v,Ive,'k');
axes2[1].plot(v,se, 'k--');
axes2[1].plot(v,Iv0e, 'k--');
axes2[1].text(88, 9.6,'$S_{\\nu}$');
axes2[1].text(88, 5.2,'$I_{\\nu}(0)$');
axes2[1].set_title('case e');
axes2[2].plot(v,Ivf,'k');
axes2[2].plot(v,sf, 'k--');
axes2[2].plot(v,Iv0f, 'k--');
axes2[2].text(88, 9.6,'$S_{\\nu}$');
axes2[2].text(88, 5.2,'$I_{\\nu}(0)$');
axes2[2].set_title('case f');
plt.show()
