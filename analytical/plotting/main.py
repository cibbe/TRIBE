import numpy as np
import matplotlib.pyplot as plt

def dAvg(delta, phi, k1t, k2t):
    terms=giveErrors(delta, phi, k1t, k2t)
    return np.sum(np.abs(terms), axis=(0,1))


def giveErrors4(delta, phi, k1t, k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[1,1]= 8*(k1t**2-k2t**2)*np.cos(2*delta)
    errors[2,2]= -16*k1t**2*np.cos(2*delta)
    errors[2,3]= 8*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*np.sqrt(k2t)*(k1t+k2t)
    errors[3,3]= 16*k2t**2*np.cos(2*delta)
    errors[4,5]= -4*np.sqrt(2)*np.exp(-1j*phi)*np.sin(2*delta)*k1t**(3/2)*np.sqrt(k2t)
    errors[4,6]= -4*np.sqrt(2)*np.exp(1j*phi)*np.sin(2*delta)*np.sqrt(k1t)*(k2t)**(3/2)
    errors[5,5]= 8*np.cos(2*delta)*k1t**2
    errors[6,6]= -8*np.cos(2*delta)*k2t**2

    return errors

def giveErrors2(delta, phi, k1t, k2t):
    errors = np.zeros((7,7), dtype=object)
    errors[1,1]= 2 * np.cos(2*delta) * (k1t**2 - k2t**2)
    errors[2,2] = 4 * k1t**2 * np.cos(2*delta)
    errors[2,3] = -2 * (k1t + k2t) * np.exp(1j*phi) * np.sin(delta*2) * np.sqrt(k1t) * np.sqrt(k2t)
    errors[3,3] = -4 * k2t**2 * np.cos(2*delta)
    errors[4,5] = np.sqrt(2) * np.exp(-1j * phi) * np.sin(2*delta) * k1t**(3/2) * np.sqrt(k2t)
    errors[4,6] = np.sqrt(2) * np.exp(1j * phi) * np.sin(2*delta) * k2t**(3/2) * np.sqrt(k1t)
    errors[5,5] = -2 * k1t**2 * np.cos(2 * delta)
    errors[6,6] = 2 * k2t**2 * np.cos(2*delta)
    
    return errors

def giveErrors(delta, phi, k1t, k2t): # Choose giverrors4 or giveerrors2 here
    return giveErrors4(delta,phi, k1t, k2t)

def main():
    delta=np.pi/2
    phi=0
    delta = np.linspace(0, 2*np.pi, 2000)
    phi = 0
    k1t=10**(-2)
    k2t=10**(-2)

    fig = plt.figure(figsize=(12,5))
    rows = fig.subfigures(2,1, hspace=0.3)

    # fig, axes = plt.subplots(2, 2, figsize=(12, 5))   # 1 row, 2 columns

    rows[0].suptitle(f"$k_1t = {k1t},  k_2t = {k2t}$", fontsize=16)
    # --- Subplot 1 ---
    cols = rows[0].subplots(1,2)
    cols[0].plot(delta, dAvg(delta, phi, k1t, k2t))

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

    cols[0].set_xticks(ticks)
    cols[0].set_xticklabels(labels)

    cols[0].set_xlabel(r"$\delta \,(\text{rad})$")
    cols[0].set_ylabel(r"$\Delta$")
    cols[0].set_title("Error difference sum")

    cols[0].set_ylim(bottom=0)

    # --- Subplot 2 ---
    errorIndexes = [[1,1], [2,2], [2,3], [3,3], [4,5], [4,6], [5,5], [6,6]]
    errorList = list(map(lambda x: "$E_" + str(x[0]) + "^\\dagger E_" + str(x[1]) + "$", errorIndexes))
    errvals = giveErrors(delta, 0, k1t, k2t)
    # for (x, errs) in enumerate(errvals):
    #     for (y, err) in enumerate(errs):
    #         if np.sum(err) > 0:
    #             print(x, y)

    for i, coord in enumerate(errorIndexes):
        cols[1].plot(delta, np.abs(errvals[coord[0], coord[1]]), label=errorList[i])

    cols[1].set_ylim(bottom=0)
    cols[1].set_xticks(ticks)
    cols[1].set_xticklabels(labels)

    cols[1].set_title("Separate errors")
    cols[1].legend(bbox_to_anchor=(1.04,0.5), loc="center left")

    # fig.text(0.5, 0.97,  # position for row 1
    #          ha="center", fontsize=16)


    # --- Subplot 3 ---
    rows[1].suptitle(f"$k_1t = {k1t},  k_2t = {k2t}$", fontsize=16)
    cols = rows[1].subplots(1,2)

    k1t=10**(-2)
    k2t=10**(-3)


    cols[0].plot(delta, dAvg(delta, phi, k1t, k2t))
    cols[0].set_ylim(bottom=0)

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

    cols[0].set_xticks(ticks)
    cols[0].set_xticklabels(labels)

    cols[0].set_xlabel(r"$\delta \,(\text{rad})$")
    cols[0].set_ylabel(r"$\Delta$")
    cols[0].set_title("Error difference sum")


    # --- Subplot 4 ---
    errvals = giveErrors(delta, 0, k1t, k2t)
    # errorList = list(map(lambda x: "$E_" + x[0] + "^\\dagger E_" + x[1] + "$", ("11", "22", "23", "33", "45", "46", "55", "66")))

    for i, coord in enumerate(errorIndexes):
        cols[1].plot(delta, np.abs(errvals[coord[0], coord[1]]), label=errorList[i])
    cols[1].set_ylim(bottom=0)
    cols[1].set_xticks(ticks)
    cols[1].set_xticklabels(labels)
    # for i, y in enumerate(giveErrors(delta, 0, k1t, k2t)):
    #     axes[1,1].plot(delta, y, label=errorList[i])

    cols[1].set_title("All errors plotted together")
    # cols[1].legend()
    cols[1].legend(bbox_to_anchor=(1.04,0.5), loc="center left")

    # plt.tight_layout(rect=[0, 0, 1, 0.92])

    # plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

#  !uv run main.py
