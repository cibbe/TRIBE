import numpy as np
import matplotlib.pyplot as plt

#Plots the different things
#For N=4 we have no off-diagonal terms, so we can just do take the difference squared for that

def get_diag_errors_N2(delta, phi, k1t, k2t):
    
    E1dE1_0011=2*np.cos(2*delta)*(k1t**2-k2t**2)
    E2dE2_0011=-4*k1t**2*np.cos(2*delta)
    E2dE3_0011=2*np.exp(1j*phi)*np.sin(2*delta)*(k1t+k2t)*np.sqrt(k1t*k2t)
    E3dE3_0011=4*k2t**2*np.cos(2*delta)
    E4dE5_0011=-np.sqrt(2)*np.exp(-1j*phi)*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)
    E4dE6_0011=-np.sqrt(2)*np.exp(1j*phi)*np.sin(2*delta)*k2t**(3/2)*np.sqrt(k1t)
    E5dE5_0011=2*k1t**2*np.cos(2*delta)
    E6dE6_0011=-2*k2t**2*np.cos(2*delta)

    return [E1dE1_0011,E2dE2_0011,E2dE3_0011,E3dE3_0011,E4dE5_0011,E4dE6_0011,E5dE5_0011,E6dE6_0011]


def get_01_terms_N2(delta, phi,k1t,k2t):
    E1dE1=1/8*(k1t**2-k2t**2)*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2
    E2dE2=-np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2*k1t*(k1t-k2t)
    E2dE3=1/2*np.sin(2*delta)*np.exp(-1j*phi)*(k1t-k2t)*np.sqrt(k1t*k2t)*(-6*(np.cos(delta))**2+np.exp(4j*phi)*(np.sin(delta)**2))
    E3dE3=np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2*k2t*(k1t-k2t)
    E4dE4=-k1t*k2t*np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2
    E4dE5=1/np.sqrt(2)*np.exp(-3j*phi)*1/2*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)*(-6*(np.sin(delta))**2+np.exp(4j*phi)*(np.cos(delta))**2)
    E4dE6=1/np.sqrt(2)*np.exp(-1j*phi)*1/2*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)*(-6*(np.cos(delta))**2+np.exp(4j*phi)*(np.sin(delta))**2)
    E5dE5=1/8*k1t**2*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2
    E5dE6=1/2*k1t*k2t*(6*(np.sin(delta))**4+np.exp(4j*phi)*(np.sin(delta))**4)
    E6dE6=1/8*k2t**2*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2

    return [E1dE1,E2dE2,E2dE3,E3dE3,E4dE4,E4dE5,E4dE6,E5dE5,E5dE6,E6dE6]

#Not including EidEi terms since they are unneeded
def get_10_terms_N2(phi,delta,k1t,k2t):
    E2dE3=1/2*np.sin(2*delta)*np.exp(-1j*phi)*(k1t-k2t)*np.sqrt(k1t*k2t)*(-(np.cos(delta))**2+6*np.exp(4j*phi)*(np.sin(delta)**2))
    E4dE5=1/np.sqrt(2)*np.exp(-3j*phi)*1/2*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)*(-(np.sin(delta))**2+6*np.exp(4j*phi)*(np.cos(delta))**2)
    E4dE6=-1/np.sqrt(2)*np.exp(-1j*phi)*1/2*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)*((np.cos(delta))**2-6*np.exp(4j*phi)*(np.sin(delta))**2)
    E5dE6=1/2*k1t*k2t*((np.sin(delta))**4+6*np.exp(4j*phi)*(np.sin(delta))**4)
    return [E2dE3,E4dE5,E4dE6,E5dE6]


def cost_function_N2(delta, phi, k1t, k2t):
    cost=0
    #Diagonal elements

    diag=get_diag_errors_N2(delta, phi, k1t, k2t)
    for term in diag:
        cost+=abs(term)**2

    # <0|O|1> elements
    off_diag01=get_01_terms_N2(delta, phi, k1t, k2t)
    off_diag10=get_10_terms_N2(delta, phi, k1t, k2t)

    for term in off_diag01:
        cost+=abs(term)**2

    for term in off_diag10:
        cost+=abs(term)**2
    
    return cost

delta = np.linspace(0, np.pi, 600)
phi = np.linspace(0,np.pi, 600)
k1t=10**(-2)
k2t=10**(-2)

ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
labels = [
    r"$0$",
    r"$\frac{\pi}{4}$",
    r"$\frac{\pi}{2}$",
    r"$\frac{3\pi}{4}$",
    r"$\pi$",
]

plt.figure(1)
plt.plot(delta,cost_function_N2(delta,0,k1t,k2t))
plt.xticks(ticks, labels)
plt.figure(2)

Delta, Phi=np.meshgrid(delta, phi)
fig, ax = plt.subplots()

im = ax.imshow(
    cost_function_N2(Delta, Phi, k1t, k2t),
    origin="lower",
    aspect="auto",
    extent=[0, np.pi, 0, np.pi]
)

# Ticks at nice multiples of pi
ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
ticklabels = ["0", "π/4", "π/2", "3π/4", "π"]

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(ticklabels)
ax.set_yticklabels(ticklabels)

ax.set_xlabel(r"$\delta$")
ax.set_ylabel(r"$\phi$")
ax.set_title("Heatmap example")

plt.colorbar(im, ax=ax, label="Value")
plt.show()