import numpy as np
from scipy import signal

PATH_W = "windowreferenzdatensatz"
PATH_R = "refspektren"


# addition aller 5 aufnahmen, mit anschliessender mittelung
LRef = (np.genfromtxt(PATH_R + "RefWinL1.csv")
+ np.genfromtxt(PATH_R + "RefWinL2.csv")
+ np.genfromtxt(PATH_R + "RefWinL3.csv")
+ np.genfromtxt(PATH_R + "RefWinL4.csv")
+ np.genfromtxt(PATH_R + "RefWinL5.csv")) / 5

# addition aller 5 aufnahmen, mit anschliessender mittelung
RRef = (np.genfromtxt(PATH_R + "RefWinR1.csv")
+ np.genfromtxt(PATH_R + "RefWinR2.csv")
+ np.genfromtxt(PATH_R + "RefWinR3.csv")
+ np.genfromtxt(PATH_R + "RefWinR4.csv")
+ np.genfromtxt(PATH_R + "RefWinR5.csv")) / 5

# addition aller 5 aufnahmen, mit anschliessender mittelung
TRef = (np.genfromtxt(PATH_R + "RefWinT1.csv")
+ np.genfromtxt(PATH_R + "RefWinT2.csv")
+ np.genfromtxt(PATH_R + "RefWinT3.csv")
+ np.genfromtxt(PATH_R + "RefWinT4.csv")
+ np.genfromtxt(PATH_R + "RefWinT5.csv")) / 5

# addition aller 5 aufnahmen, mit anschliessender mittelung
HRef = (np.genfromtxt(PATH_R + "RefWinH1.csv")
+ np.genfromtxt(PATH_R + "RefWinH2.csv")
+ np.genfromtxt(PATH_R + "RefWinH3.csv")
+ np.genfromtxt(PATH_R + "RefWinH4.csv")
+ np.genfromtxt(PATH_R + "RefWinH5.csv")) / 5

# speichern der gemittelten referenzspektren
def safeRefWAsCSV(eingangssignal):
    csvRefArray = np.savetxt(PATH_R + "/decodedtrigR1.csv", eingangssignal, delimiter=",")
    return csvRefArray

safeRefWAsCSV(LRef)
