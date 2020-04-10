#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
Data_Vce_Ic_Ic_125C = [1.94E+01,
7.43E+01,
1.61E+02,
3.49E+02,
4.52E+02,
5.91E+02,
6.94E+02,
8.20E+02,
9.20E+02,
9.98E+02,
1.05E+03,
1.12E+03,
1.17E+03,
1.25E+03,
1.34E+03,
1.48E+03,
1.61E+03,
1.73E+03,
1.88E+03,
2.02E+03
]
Data_Vce_Ic_Vce_125C = [6.05E-01,
7.58E-01,
9.03E-01,
1.11E+00,
1.21E+00,
1.33E+00,
1.40E+00,
1.50E+00,
1.56E+00,
1.61E+00,
1.65E+00,
1.69E+00,
1.72E+00,
1.77E+00,
1.83E+00,
1.91E+00,
1.99E+00,
2.06E+00,
2.15E+00,
2.23E+00
]
Data_Vce_Ic_Ic_175C = [3.55E+01,
6.13E+01,
9.69E+01,
1.39E+02,
1.84E+02,
2.62E+02,
3.23E+02,
4.33E+02,
5.36E+02,
6.49E+02,
7.75E+02,
9.01E+02,
1.02E+03,
1.14E+03,
1.26E+03,
1.38E+03,
1.51E+03,
1.64E+03,
1.77E+03,
1.90E+03,
2.02E+03
]
Data_Vce_Ic_Vce_175C = [5.92E-01,
6.71E-01,
7.50E-01,
8.29E-01,
9.03E-01,
1.02E+00,
1.09E+00,
1.21E+00,
1.32E+00,
1.43E+00,
1.54E+00,
1.64E+00,
1.73E+00,
1.83E+00,
1.92E+00,
2.01E+00,
2.10E+00,
2.19E+00,
2.28E+00,
2.37E+00,
2.46E+00
]

Data_Vf_If_If_125C = [2.26E+01,
1.00E+02,
1.87E+02,
2.94E+02,
4.14E+02,
5.14E+02,
6.11E+02,
7.27E+02,
8.56E+02,
9.86E+02,
1.12E+03,
1.27E+03,
1.39E+03,
1.52E+03,
1.63E+03,
1.83E+03,
2.16E+03
]
Data_Vf_If_Vf_125C = [5.79E-01,
7.37E-01,
8.41E-01,
9.38E-01,
1.03E+00,
1.10E+00,
1.16E+00,
1.22E+00,
1.29E+00,
1.35E+00,
1.42E+00,
1.48E+00,
1.54E+00,
1.59E+00,
1.63E+00,
1.71E+00,
1.83E+00
]
Data_Vf_If_If_175C = [2.59E+01,
7.43E+01,
1.55E+02,
2.55E+02,
3.62E+02,
4.78E+02,
5.78E+02,
7.04E+02,
8.01E+02,
8.98E+02,
1.00E+03,
1.11E+03,
1.21E+03,
1.33E+03,
1.48E+03,
1.63E+03,
1.76E+03,
1.92E+03,
2.06E+03,
2.23E+03
]
Data_Vf_If_Vf_175C = [4.88E-01,
6.07E-01,
7.28E-01,
8.36E-01,
9.27E-01,
1.02E+00,
1.09E+00,
1.16E+00,
1.22E+00,
1.27E+00,
1.33E+00,
1.38E+00,
1.43E+00,
1.49E+00,
1.56E+00,
1.63E+00,
1.68E+00,
1.75E+00,
1.80E+00,
1.88E+00
]

#
p1_vce_ic_125c=-1.891e-07
p2_vce_ic_125c=0.001124
p3_vce_ic_125c=0.6882

p1_vce_ic_175c=-2.158e-07
p2_vce_ic_175c=0.001312
p3_vce_ic_175c=0.6398

p1_vf_if_125c= -1.638e-07
p2_vf_if_125c=  0.0008779
p3_vf_if_125c=     0.6562
    
p1_vf_if_175c=-1.621e-07
p2_vf_if_175c= 0.0009296
p3_vf_if_175c=    0.5668

#
x=[float(i) for i in range(2000)]
y_vce_ic_125c=[p1_vce_ic_125c*i*i+p2_vce_ic_125c*i+p3_vce_ic_125c for i in x]
y_vce_ic_175c=[p1_vce_ic_175c*i*i+p2_vce_ic_175c*i+p3_vce_ic_175c for i in x]
y_vf_if_125c=[p1_vf_if_125c*i*i+p2_vf_if_125c*i+p3_vf_if_125c for i in x]
y_vf_if_175c=[p1_vf_if_175c*i*i+p2_vf_if_175c*i+p3_vf_if_175c for i in x]




#
plt.figure()
plt.subplot(2,2,1)
plt.plot(Data_Vce_Ic_Ic_125C,Data_Vce_Ic_Vce_125C,'o')
plt.plot(x,y_vce_ic_125c,label="vce_ic_125c")
plt.legend()
plt.grid()

plt.subplot(2,2,2)
plt.plot(Data_Vce_Ic_Ic_175C,Data_Vce_Ic_Vce_175C,'o')
plt.plot(x,y_vce_ic_175c,label="vce_ic_175c")
plt.legend()
plt.grid()

plt.subplot(2,2,3)
plt.plot(Data_Vf_If_If_125C,Data_Vf_If_Vf_125C,'o')
plt.plot(x,y_vf_if_125c,label="vf_if_125c")
plt.legend()
plt.grid()

plt.subplot(2,2,4)
plt.plot(Data_Vf_If_If_175C,Data_Vf_If_Vf_175C,'o')
plt.plot(x,y_vf_if_125c,label="vf_if_175c")
plt.legend()
plt.grid()

plt.show()

























