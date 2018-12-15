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

y_trial = 50 * a * np.array([4,5,6,7,8,9,10])
x_trial = -100 * y_trial 
v_trial = 10**6*np.linspace(0.5,1,7)
pos_ps_max = []
v_ps_max = []


for i in range(0,7):
    pos_x = np.zeros(step)
    pos_y = np.zeros(step)
    v_x = np.zeros(step)
    v_x[0]=v0
    v_y = np.zeros(step)
    a_x = np.zeros(step)
    a_y = np.zeros(step)
    dist = np.zeros(step)
    dist[0] = x_trial[i]
    pos_x[0] = x_trial[i]
    pos_y[0] = y_trial[i]

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
    freq, ps = scipy.signal.periodogram(a_x,step/dt)
    pos_ps_max.append(freq[np.argmax(ps)])
    

for i in range(0,7):
    pos_x = np.zeros(step)
    pos_y = np.zeros(step)
    v_x = np.zeros(step)
    v_x[0]=v_trial[i]
    v_y = np.zeros(step)
    a_x = np.zeros(step)
    a_y = np.zeros(step)
    dist = np.zeros(step)
    dist[0] = -35000*a
    pos_x[0] = dist[0]
    pos_y[0] = 350*a

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
    freq, ps = scipy.signal.periodogram(a_x,step/dt)
    v_ps_max.append(freq[np.argmax(ps)])
    
np.array(pos_ps_max)
np.array(v_ps_max)

plt.gcf().clear()
plt.plot(y_trial, pos_ps_max);plt.savefig('impact_change.png')
plt.gcf().clear()
plt.plot(v_trial, v_ps_max);plt.savefig('v_change.png')
plt.gcf().clear()
