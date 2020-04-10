#
#
#
import numpy as np
import matplotlib.pyplot as plt

#
Erec_Rg_Rg_125C = [1.24E+00,1.43E+00,1.59E+00,1.78E+00,1.98E+00,2.15E+00,2.36E+00,2.56E+00,2.76E+00,2.99E+00,3.19E+00,3.41E+00,3.63E+00,3.85E+00,4.06E+00,4.28E+00,4.50E+00,4.73E+00,4.97E+00,5.20E+00,5.43E+00,5.70E+00,5.94E+00,6.18E+00,6.41E+00,6.66E+00,6.89E+00,7.10E+00,7.37E+00,7.62E+00,7.85E+00,8.10E+00,8.35E+00,8.58E+00,8.80E+00]
Erec_Rg_Erec_125C = [2.04E+02,1.98E+02,1.93E+02,1.87E+02,1.81E+02,1.77E+02,1.72E+02,1.67E+02,1.63E+02,1.58E+02,1.54E+02,1.50E+02,1.47E+02,1.44E+02,1.41E+02,1.38E+02,1.35E+02,1.33E+02,1.31E+02,1.29E+02,1.27E+02,1.25E+02,1.24E+02,1.23E+02,1.22E+02,1.21E+02,1.20E+02,1.20E+02,1.19E+02,1.19E+02,1.18E+02,1.17E+02,1.17E+02,1.17E+02,1.16E+02]

Erec_Rg_Rg_150C = [1.22E+00,1.44E+00,1.66E+00,1.86E+00,2.08E+00,2.34E+00,2.59E+00,2.85E+00,3.12E+00,3.40E+00,3.64E+00,3.95E+00,4.22E+00,4.46E+00,4.77E+00,5.13E+00,5.45E+00,5.81E+00,6.15E+00,6.47E+00,6.81E+00,7.15E+00,7.41E+00,7.61E+00,7.88E+00,8.14E+00,8.41E+00,8.61E+00,8.85E+00]
Erec_Rg_Erec_150C = [2.44E+02,2.36E+02,2.28E+02,2.21E+02,2.14E+02,2.06E+02,1.99E+02,1.92E+02,1.86E+02,1.80E+02,1.75E+02,1.70E+02,1.66E+02,1.63E+02,1.58E+02,1.55E+02,1.52E+02,1.49E+02,1.47E+02,1.46E+02,1.44E+02,1.43E+02,1.42E+02,1.42E+02,1.41E+02,1.40E+02,1.40E+02,1.39E+02,1.39E+02]
#
p1_125C = -0.2167
p2_125C = 5.344
p3_125C = -45.79
p4_125C = 253

p1_150C = -0.255
p2_150C = 6.313
p3_150C = -54.31
p4_150C = 301.7


xList = [float(i/100*9) for i in range(12,100)]
y1List = [p1_125C*i*i*i+p2_125C*i*i+p3_125C*i+p4_125C for i in xList]
y2List = [p1_150C*i*i*i+p2_150C*i*i+p3_150C*i+p4_150C for i in xList]

plt.figure()
plt.subplot(2,1,1)
plt.plot(Erec_Rg_Rg_125C, Erec_Rg_Erec_125C, "r*-")
plt.plot(xList,y1List)

plt.plot(Erec_Rg_Rg_150C, Erec_Rg_Erec_150C, "r*-")
plt.plot(xList,y2List)

plt.grid()

plt.subplot(2,1,2)
plt.plot(Erec_Rg_Rg_150C, Erec_Rg_Erec_150C, "r*-")
plt.plot(xList,y2List)
plt.grid()


plt.show()