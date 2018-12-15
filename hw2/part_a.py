pc = (3.086 *10**18)    #[cm] 
D = (100 * pc )
n = 1                   #[cm^-3]

#Using the definition of Column Density N = n*l 

N = (n*D)

#Using def \tau = N \sigma_\nu 

sig_a = 10**(-3)/N  
sig_b = 1/N
sig_c = 10**3/N 

print 'The column density is {} cm^-2' .format(N)
print 'the cross section for a total optical depth of a), b), c) are given by {a} cm^-2,{b} cm^-2,{c} cm^-2 respectively' .format(a=sig_a, b=sig_b,c=sig_c)
