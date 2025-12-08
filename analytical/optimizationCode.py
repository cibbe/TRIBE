# Error correction project
#dEiEj=<0|EiEj|0>-<1|EiEj|1>

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

delta=np.pi/2
phi=0


def dAvg(delta, phi, k1t, k2t):
    terms=giveErrors(delta, phi, k1t, k2t)
    return abs(sum(terms))

def giveErrors(delta,phi, k1t, k2t):
    dE1E1=8*(k1t**2-k2t**2)*np.cos(2*delta)
    dE2E2=-16*k1t**2*np.cos(2*delta)
    dE2E3=8*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*np.sqrt(k2t)*(k1t+k2t)
    dE3E3=16*k2t**2*np.cos(2*delta)
    dE4E5=-4*np.sqrt(2)*np.exp(-1j*phi)*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)
    dE4E6=-4*np.sqrt(2)*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)
    dE5E5=8*np.cos(2*delta)*k1t**2
    dE6E6=-8*np.cos(2*delta)*k2t**2   

    terms = [
        dE1E1, dE2E2, dE2E3, dE3E3,
        dE4E5, dE4E6,
        dE5E5, dE6E6
    ]
    terms = [abs(x) for x in terms]
    return terms


delta = np.linspace(0, 2*np.pi, 2000)
phi = 0
k1t=10**(-2)
k2t=10**(-2)

fig, axes = plt.subplots(2, 2, figsize=(12, 5))   # 1 row, 2 columns

# --- Subplot 1 ---
axes[0,0].plot(delta, dAvg(delta, phi, k1t, k2t))

ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
labels = [
    r"$0$",
    r"$\frac{\pi}{4}$",
    r"$\frac{\pi}{2}$",
    r"$\frac{3\pi}{4}$",
    r"$\pi$",
    r"$\frac{5\pi}{4}$",
    r"$\frac{3\pi}{2}$",
    r"$\frac{7\pi}{4}$", 
    r"$2\pi$"
]

axes[0,0].set_xticks(ticks)
axes[0,0].set_xticklabels(labels)

axes[0,0].set_xlabel(r"$\delta \,(\text{rad})$")
axes[0,0].set_ylabel(r"$\Delta$")
axes[0,0].set_title("The average error difference")


# --- Subplot 2 ---
errorList = ["E1dE1", "E2dE2", "E2dE3", "E3dE3", "E4dE5", "E4dE6", "E5dE5", "E6dE6"]

for i, y in enumerate(giveErrors(delta, 0, k1t, k2t)):
    axes[0,1].plot(delta, y, label=errorList[i])

axes[0,1].set_title("All errors plotted together")
axes[0,1].legend()

fig.text(0.5, 0.97,  # position for row 1
         f"k1t = {k1t},  k2t = {k2t}",
         ha="center", fontsize=16)

# --- Subplot 3 ---

k1t=10**(-2)
k2t=10**(-3)


axes[1,0].plot(delta, dAvg(delta, phi, k1t, k2t))

ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
labels = [
    r"$0$",
    r"$\frac{\pi}{4}$",
    r"$\frac{\pi}{2}$",
    r"$\frac{3\pi}{4}$",
    r"$\pi$",
    r"$\frac{5\pi}{4}$",
    r"$\frac{3\pi}{2}$",
    r"$\frac{7\pi}{4}$", 
    r"$2\pi$"
]

axes[1,0].set_xticks(ticks)
axes[1,0].set_xticklabels(labels)

axes[1,0].set_xlabel(r"$\delta \,(\text{rad})$")
axes[1,0].set_ylabel(r"$\Delta$")
axes[1,0].set_title("The average error difference")


# --- Subplot 4 ---
errorList = ["E1dE1", "E2dE2", "E2dE3", "E3dE3", "E4dE5", "E4dE6", "E5dE5", "E6dE6"]

for i, y in enumerate(giveErrors(delta, 0, k1t, k2t)):
    axes[1,1].plot(delta, y, label=errorList[i])

axes[1,1].set_title("All errors plotted together")
axes[1,1].legend()


fig.text(0.5, 0.50,  # position for row 2
         f"k1t = {k1t},  k2t = {k2t}",
         ha="center", fontsize=16)

plt.tight_layout(rect=[0, 0, 1, 0.92])

plt.tight_layout()
plt.show()