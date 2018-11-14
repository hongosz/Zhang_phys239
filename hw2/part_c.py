#Define Gaussian Shape scaled with input cross section 
def gaussian(v,sig_0):
    return sig_0*np.exp(-np.power(v-50 , 2.) / (2 * np.power(5, 2.)))

v=np.linspace(0,100,100)       #Define a range of frequency 

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10,3))
axes[0].plot(v,gaussian(v,sig_a),'k');
axes[0].set_title('$\sigma_{a}$')
axes[0].set_xlabel('$\\nu$')
axes[1].plot(v,gaussian(v,sig_b),'k');
axes[1].set_title('$\sigma_{b}$')
axes[1].set_xlabel('$\\nu$')
axes[2].plot(v,gaussian(v,sig_c),'k');
axes[2].set_title('$\sigma_{c}$')
axes[2].set_xlabel('$\\nu$')

plt.show()
