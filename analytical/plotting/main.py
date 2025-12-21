import numpy as np
import matplotlib.pyplot as plt

def giveErrorsDiag_N4(delta, phi, k1t, k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[1,1]= 8*(k1t**2-k2t**2)*np.cos(2*delta)
    errors[2,2]= -16*k1t**2*np.cos(2*delta)
    errors[2,3]= 8*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*np.sqrt(k2t)*(k1t+k2t)
    errors[3,3]= 16*k2t**2*np.cos(2*delta)
    errors[4,5]= -4*np.sqrt(2)*np.exp(-1j*phi)*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)
    errors[4,6]= -4*np.sqrt(2)*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)
    errors[5,5]= 8*np.cos(2*delta)*k1t**2
    errors[6,6]= -8*np.cos(2*delta)*k2t**2

    return errors + errors.T - np.diag(errors)

def giveErrorsDiag_N2(delta, phi, k1t, k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[1,1]= 2 * np.cos(2*delta) * (k1t**2 - k2t**2)
    errors[2,2] = 4 * k1t**2 * np.cos(2*delta)
    errors[2,3] = -2 * (k1t + k2t) * np.exp(1j*phi) * np.sin(delta*2) * np.sqrt(k1t) * np.sqrt(k2t)
    errors[3,3] = -4 * k2t**2 * np.cos(2*delta)
    errors[4,5] = np.sqrt(2) * np.exp(-1j * phi) * np.sin(2*delta) * k1t**(3/2) * np.sqrt(k2t)
    errors[4,6] = np.sqrt(2) * np.exp(1j * phi) * np.sin(2*delta) * k2t**(3/2) * np.sqrt(k1t)
    errors[5,5] = -2 * k1t**2 * np.cos(2 * delta)
    errors[6,6] = 2 * k2t**2 * np.cos(2*delta)
    
    # Mirror over diagonal
    return errors + errors.T - np.diag(errors)

def giveErrors01_N2(delta, phi,k1t,k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[1,1]=1/8*(k1t**2-k2t**2)*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2
    errors[2,2]=-np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2*k1t*(k1t-k2t)
    errors[2,3]=1/2*np.sin(2*delta)*np.exp(-1j*phi)*(k1t-k2t)*np.sqrt(k1t*k2t)*(-6*(np.cos(delta))**2+np.exp(4j*phi)*(np.sin(delta)**2))
    errors[3,3]=np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2*k2t*(k1t-k2t)
    errors[4,4]=-k1t*k2t*np.exp(-2j*phi)*(6+np.exp(4j*phi))*1/4*(np.sin(2*delta))**2
    errors[4,5]=1/np.sqrt(2)*np.exp(-3j*phi)*1/2*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)*(-6*(np.sin(delta))**2+np.exp(4j*phi)*(np.cos(delta))**2)
    errors[4,6]=1/np.sqrt(2)*np.exp(-1j*phi)*1/2*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)*(-6*(np.cos(delta))**2+np.exp(4j*phi)*(np.sin(delta))**2)
    errors[5,5]=1/8*k1t**2*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2
    errors[5,6]=1/2*k1t*k2t*(6*(np.sin(delta))**4+np.exp(4j*phi)*(np.sin(delta))**4)
    errors[6,6]=1/8*k2t**2*np.exp(-2j*phi)*(6+np.exp(4j*phi))*(np.sin(2*delta))**2
    return errors

#Not including EidEi terms since they are unneeded
def giveErrors10_N2(phi,delta,k1t,k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[2,3]=1/2*np.sin(2*delta)*np.exp(-1j*phi)*(k1t-k2t)*np.sqrt(k1t*k2t)*(-(np.cos(delta))**2+6*np.exp(4j*phi)*(np.sin(delta)**2))
    errors[4,5]=1/np.sqrt(2)*np.exp(-3j*phi)*1/2*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)*(-(np.sin(delta))**2+6*np.exp(4j*phi)*(np.cos(delta))**2)
    errors[4,6]=-1/np.sqrt(2)*np.exp(-1j*phi)*1/2*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)*((np.cos(delta))**2-6*np.exp(4j*phi)*(np.sin(delta))**2)
    errors[5,6]=1/2*k1t*k2t*((np.sin(delta))**4+6*np.exp(4j*phi)*(np.sin(delta))**4)
    return errors

# Join the upper and lower halves
def giveErrorsOffDiag_N2(phi, delta, k1t, k2t):
    return giveErrors01_N2(phi, delta, k1t, k2t) + giveErrors10_N2(phi, delta, k1t, k2t).T

def errsum_N2(delta,phi,k1t, k2t):
    return np.abs(giveErrorsDiag_N2(delta, phi, k1t, k2t))**2 + np.abs(giveErrorsOffDiag_N2(delta, phi, k1t, k2t))**2 * 2


def main():
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

    fig, (ax1, ax2) = plt.subplots(ncols=2)

    Delta, Phi=np.meshgrid(delta, phi)
    im = ax1.imshow(
        np.sum(errsum_N2(Delta, Phi, k1t, k2t)),
        origin="lower",
        aspect="auto",
        extent=[0, np.pi, 0, np.pi]
    )
    fig.suptitle("$N=2, k_1=k_2=0.01$")

    fig.colorbar(im, label="Cost sum")
    ax1.set_title("Cost depent on beam splitter parameters")
    ax1.set_xticks(ticks, labels)
    ax1.set_yticks(ticks, labels)
    ax1.set_xlabel("$\\delta$ [rad]")
    ax1.set_ylabel("$\\phi$ [rad]")
    ax1.set_box_aspect(1)

    ax2.set_title("Cost for optimal $\\phi=\\pi/4$")
    ax2.plot(delta,np.sum(errsum_N2(delta,np.pi/4,k1t,k2t)))
    ax2.set_xticks(ticks, labels)
    ax2.set_xlabel("$\\delta$ [rad]")
    ax2.set_ylabel("Cost sum")
    ax2.set_box_aspect(1)



    plt.show()


if __name__ == "__main__":
    main()

#  !uv run main.py
