import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt 

me = (9.11*10**(-31))     #mass of electron [kg] 
Z = 10    
k = (8.99 * 10**9)
a = (5.29 * 10**(-11))    #Bohr radius [m]
e = (1.6*10**(-19))       #charge of an electron 


step = 10000           #number of steps in time 
v0 = (1.5*10**6)            #initial velocity of electron [m/s]
#dt = 1000*a/v0/step 


pos_x = np.zeros(step)
pos_y = np.zeros(step)
v_x = np.zeros(step)
v_x[0]=v0
v_y = np.zeros(step)
a_x = np.zeros(step)
a_y = np.zeros(step)
dist = np.zeros(step)
dist[0] = -25000*a
pos_x[0] = dist[0]
pos_y[0] = 250*a
#theta = np.zeros(step)
#theta[0] = np.arctan(pos_y[0]/pos_x[0])

dt = (2*np.abs(dist[0])/v0/step)

time = np.arange(0,step)*dt


for i in range(1,step):
    F = k * 10 * e * e/((dist[i-1])**2)
    a_x[i-1] = -F*np.cos(np.arctan2(pos_y[i-1],pos_x[i-1]))/me
    v_x[i] = v_x[i-1] + a_x[i-1] * dt 
    pos_x[i] = pos_x[i-1] + v_x[i-1] *dt 
    a_y[i-1] = -F*np.sin(np.arctan2(pos_y[i-1],pos_x[i-1]))/me
    v_y[i] = v_y[i-1] + a_y[i-1] * dt 
    pos_y[i] = pos_y[i-1] + v_y[i-1] *dt
    dist[i]= (pos_x[i]**2 + pos_y[i]**2)**0.5
    
plt.gcf().clear()
plt.plot(pos_x/a,pos_y/a,);
plt.xlabel('pos_x$(a_0)$')
plt.ylabel('pos_y($a_0$)')
plt.savefig('Position.png')
plt.gcf().clear()

plt.plot(time,v_x,label="v_x");
plt.plot(time,v_y,label="v_y");
plt.legend(loc=5)
plt.xlabel('$v_x(m/s)$')
plt.ylabel('$v_y(m/s)$')
plt.savefig('Velocity.png')
plt.gcf().clear()


plt.plot(time,a_x,label="a_x");
plt.plot(time,a_y,label="a_y");
plt.legend(loc=5)
plt.xlabel('$a_x(m/s^2)$')
plt.ylabel('$a_y(m/s^2)$')
plt.savefig('Acceleration.png')
plt.gcf().clear()


freq, ps = scipy.signal.periodogram(a_x,step/dt)
plt.plot(freq,ps,'.');
plt.xlim([-0.05E19,0.1E19]);
plt.xlabel('$\omega$ rad/s)')
plt.ylabel('Amplitude')
plt.savefig('PowerSepc.png')
plt.gcf().clear()
