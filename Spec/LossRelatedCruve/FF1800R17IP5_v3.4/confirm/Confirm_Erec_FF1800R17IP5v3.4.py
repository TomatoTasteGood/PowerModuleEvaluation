#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
Data_Erec_If_If_125C=[1.86E+02,
2.73E+02,
3.64E+02,
4.39E+02,
5.26E+02,
6.12E+02,
7.20E+02,
8.15E+02,
9.27E+02,
1.03E+03,
1.15E+03,
1.29E+03,
1.46E+03,
1.64E+03,
1.80E+03,
2.06E+03
]
Data_Erec_If_Erec_125C=[1.12E+02,
1.37E+02,
1.62E+02,
1.80E+02,
2.00E+02,
2.18E+02,
2.39E+02,
2.55E+02,
2.73E+02,
2.87E+02,
3.03E+02,
3.19E+02,
3.37E+02,
3.52E+02,
3.65E+02,
3.82E+02
]
Data_Erec_If_If_175C=[1.94E+02,
2.86E+02,
3.52E+02,
4.55E+02,
5.54E+02,
6.70E+02,
7.86E+02,
9.19E+02,
1.13E+03,
1.28E+03,
1.44E+03,
1.61E+03,
1.78E+03,
1.95E+03,
2.14E+03
]
Data_Erec_If_Erec_175C=[1.63E+02,
1.93E+02,
2.15E+02,
2.47E+02,
2.74E+02,
3.04E+02,
3.30E+02,
3.58E+02,
3.94E+02,
4.18E+02,
4.40E+02,
4.59E+02,
4.78E+02,
4.94E+02,
5.10E+02
]

Data_Erec_Rg_Rg_125C=[5.62E-01,
7.48E-01,
9.97E-01,
1.22E+00,
1.49E+00,
1.74E+00,
2.00E+00,
2.25E+00,
2.50E+00,
2.74E+00,
3.00E+00,
3.29E+00,
3.56E+00,
3.76E+00,
4.01E+00
]
Data_Erec_Rg_Erec_125C=[3.64E+02,
3.41E+02,
3.15E+02,
2.96E+02,
2.79E+02,
2.66E+02,
2.54E+02,
2.45E+02,
2.36E+02,
2.28E+02,
2.21E+02,
2.12E+02,
2.05E+02,
2.00E+02,
1.94E+02
]
Data_Erec_Rg_Rg_175C=[5.60E-01,
7.95E-01,
9.95E-01,
1.21E+00,
1.48E+00,
1.71E+00,
1.98E+00,
2.22E+00,
2.48E+00,
2.76E+00,
3.00E+00,
3.29E+00,
3.54E+00,
3.86E+00,
4.28E+00
]
Data_Erec_Rg_Erec_175C=[4.80E+02,
4.50E+02,
4.27E+02,
4.06E+02,
3.82E+02,
3.65E+02,
3.48E+02,
3.33E+02,
3.20E+02,
3.07E+02,
2.96E+02,
2.85E+02,
2.77E+02,
2.66E+02,
2.53E+02
]

p1_erec_if_125c=-6.11e-05
p2_erec_if_125c=0.2752 
p3_erec_if_125c=68.95


p1_erec_if_175c=-6.918e-05
p2_erec_if_175c= 0.3336 
p3_erec_if_175c=106.6 


p1_erec_rg_125c=-4.841
p2_erec_rg_125c=45.04
p3_erec_rg_125c=-165
p4_erec_rg_125c=441.3
         
p1_erec_rg_175c=-3.118 
p2_erec_rg_175c=35.23
p3_erec_rg_175c= -165.9 
p4_erec_rg_175c= 561.3

x_if = [float(i) for i in range(2500)]
x_rg = [float(i/10) for i in range(50)]
y_erec_if_125c=[p1_erec_if_125c*i*i+p2_erec_if_125c*i+p3_erec_if_125c for i in x_if]
y_erec_if_175c=[p1_erec_if_175c*i*i+p2_erec_if_175c*i+p3_erec_if_175c for i in x_if]
y_erec_rg_125c=[p1_erec_rg_125c*i*i*i+p2_erec_rg_125c*i*i+p3_erec_rg_125c*i+p4_erec_rg_125c for i in x_rg]
y_erec_rg_175c=[p1_erec_rg_175c*i*i*i+p2_erec_rg_175c*i*i+p3_erec_rg_175c*i+p4_erec_rg_175c for i in x_rg]


plt.figure()
plt.subplot(2,2,1)
plt.plot(x_if,y_erec_if_125c,label='erec_if_125c')
plt.plot(Data_Erec_If_If_125C, Data_Erec_If_Erec_125C,'o')
plt.legend()
plt.grid()

plt.subplot(2,2,2)
plt.plot(x_if,y_erec_if_175c,label='erec_if_175c')
plt.plot(Data_Erec_If_If_175C, Data_Erec_If_Erec_175C,'o')
plt.legend()
plt.grid()

plt.subplot(2,2,3)
plt.plot(x_rg,y_erec_rg_125c,label='erec_rg_125c')
plt.plot(Data_Erec_Rg_Rg_125C, Data_Erec_Rg_Erec_125C,'o')
plt.legend()
plt.grid()

plt.subplot(2,2,4)
plt.plot(x_rg,y_erec_rg_175c,label='erec_rg_175c')
plt.plot(Data_Erec_Rg_Rg_125C, Data_Erec_Rg_Erec_175C,'o')
plt.legend()
plt.grid()

plt.show()









