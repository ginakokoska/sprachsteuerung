import matplotlib.pyplot as plt
import numpy as np



# plotten der referenz spektren
PATH_R = "refspektren"

LRef =  np.genfromtxt(PATH_R + "/LRef.csv")
RRef =  np.genfromtxt(PATH_R + "/RRef.csv")
HRef =  np.genfromtxt(PATH_R + "/HRef.csv")
TRef =  np.genfromtxt(PATH_R + "/TRef.csv")

fig1, axs = plt.subplots(2)
axs[0].plot(LRef)
axs[0].set_title("Links")
axs[1].plot(RRef)
axs[1].set_title("Rechts")


fig2, axs = plt.subplots(2)
axs[0].plot(HRef)
axs[0].set_title("Hoch")
axs[1].plot(TRef)
axs[1].set_title("Tief")

plt.show()
