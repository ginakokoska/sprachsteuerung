import numpy as np
import scipy.stats as sst


PATH_R = "refspektren"
PATH_G = "sprechergina"
PATH_E = "sprecherelena"

# Referenzdatensatz
LRef = np.genfromtxt(PATH_R + "/LRef.csv")
RRef = np.genfromtxt(PATH_R + "/RRef.csv")
TRef = np.genfromtxt(PATH_R + "/TRef.csv")
HRef = np.genfromtxt(PATH_R + "/HRef.csv")

# selber sprecher wie referenz
LG = np.genfromtxt(PATH_G + "/winL.csv")
RG = np.genfromtxt(PATH_G + "/winR.csv")
TG = np.genfromtxt(PATH_G + "/winT.csv")
HG = np.genfromtxt(PATH_G + "/winH.csv")

# anderer sprecher wie referenz
LE = np.genfromtxt(PATH_E + "/winL.csv")
RE = np.genfromtxt(PATH_E + "/winR.csv")
TE = np.genfromtxt(PATH_E + "/winT.csv")
HE = np.genfromtxt(PATH_E + "/winH.csv")


# korrelation datensatz mit selben sprecher
korrkoefLLG = sst.pearsonr(LRef, LG)[0]
korrkoefLRG = sst.pearsonr(LRef, RG)[0]
korrkoefLTG = sst.pearsonr(LRef, TG)[0]
korrkoefLHG = sst.pearsonr(LRef, HG)[0]

# korrelation datensatz mit anderem sprecher
korrkoefLLE = sst.pearsonr(LRef, LE)[0]
korrkoefLRE = sst.pearsonr(LRef, RE)[0]
korrkoefLTE = sst.pearsonr(LRef, TE)[0]
korrkoefLHE = sst.pearsonr(LRef, HE)[0]


# berechne welches wort am besten erkannt wird original sprecher
maxValG = max(max(korrkoefLLG, korrkoefLRG),max(korrkoefLTG, korrkoefLHG))


# berechne welches wort am besten erkannt wird anderer sprecher
maxValE = max(max(korrkoefLLE, korrkoefLRE),max(korrkoefLTE, korrkoefLHE))


print(korrkoefLTG)
print(korrkoefLLG)
print(korrkoefLHG)
print(korrkoefLRG)
print(maxValG)

print(korrkoefLTE)
print(korrkoefLLE)
print(korrkoefLHE)
print(korrkoefLRE)
print(maxValE)
