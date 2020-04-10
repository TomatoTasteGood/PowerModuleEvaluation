#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Erec_Rg_125C_O3 = -0.005789
p2_Erec_Rg_125C_O3 = 0.7302
p3_Erec_Rg_125C_O3 =  -14.24
p4_Erec_Rg_125C_O3 = 155.3

p1_Erec_Rg_150C_O3 = 0.02387
p2_Erec_Rg_150C_O3 = 0.2972
p3_Erec_Rg_150C_O3 = -13.58
p4_Erec_Rg_150C_O3 = 175.2

p1_Rate_Erec_Rg_125C_O3 = -4.083e-05
p2_Rate_Erec_Rg_125C_O3 = 0.00515
p3_Rate_Erec_Rg_125C_O3 = -0.1004
p4_Rate_Erec_Rg_125C_O3 = 1.095

p1_Rate_Erec_Rg_150C_O3 = 0.0001474
p2_Rate_Erec_Rg_150C_O3 = 0.001835
p3_Rate_Erec_Rg_150C_O3 = -0.08386
p4_Rate_Erec_Rg_150C_O3 = 1.082


#
Data_Sample_Erec_Rg_Erec_125C = [1.416517E+02,
1.357271E+02,
1.298025E+02,
1.244165E+02,
1.190305E+02,
1.143627E+02,
1.096948E+02,
1.053860E+02,
1.017953E+02,
9.748654E+01,
9.461400E+01,
9.192101E+01,
8.940754E+01,
8.689408E+01,
8.491921E+01,
8.312388E+01,
8.150808E+01,
8.043088E+01,
7.917415E+01
]
Data_Sample_Erec_Rg_Rg_125C = [1.010333E+00,
1.490241E+00,
1.982778E+00,
2.475316E+00,
2.993111E+00,
3.473020E+00,
3.990815E+00,
4.508611E+00,
4.963261E+00,
5.607348E+00,
6.036739E+00,
6.529277E+00,
7.021814E+00,
7.526980E+00,
8.019518E+00,
8.575201E+00,
9.118255E+00,
1.000230E+01,
1.092423E+01
]

Data_Sample_Erec_Rg_Erec_150C = [1.617594E+02,
1.545781E+02,
1.491921E+02,
1.434470E+02,
1.380610E+02,
1.326750E+02,
1.274686E+02,
1.222621E+02,
1.175943E+02,
1.131059E+02,
1.095153E+02,
1.055655E+02,
1.025135E+02,
9.928187E+01,
9.748654E+01,
9.551167E+01,
9.425494E+01,
9.353680E+01,
9.281867E+01
]
Data_Sample_Erec_Rg_Rg_150C = [1.022962E+00,
1.553387E+00,
2.008037E+00,
2.513203E+00,
2.980482E+00,
3.473020E+00,
3.990815E+00,
4.495982E+00,
5.001148E+00,
5.544202E+00,
5.998852E+00,
6.554535E+00,
7.059701E+00,
7.628014E+00,
8.032147E+00,
8.638347E+00,
9.156142E+00,
9.989667E+00,
1.076005E+01
]



#
Data_Fit_Rg = [i/10 for i in range(110)]
Data_Fit_Erec_125C = [p1_Erec_Rg_125C_O3*i**3+p2_Erec_Rg_125C_O3*i**2+p3_Erec_Rg_125C_O3*i+p4_Erec_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Fit_Erec_150C = [p1_Erec_Rg_150C_O3*i**3+p2_Erec_Rg_150C_O3*i**2+p3_Erec_Rg_150C_O3*i+p4_Erec_Rg_150C_O3 for i in Data_Fit_Rg]

Data_Rate_Erec_125C = [p1_Rate_Erec_Rg_125C_O3*i**3+p2_Rate_Erec_Rg_125C_O3*i**2+p3_Rate_Erec_Rg_125C_O3*i+p4_Rate_Erec_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Rate_Erec_150C = [p1_Rate_Erec_Rg_150C_O3*i**3+p2_Rate_Erec_Rg_150C_O3*i**2+p3_Rate_Erec_Rg_150C_O3*i+p4_Rate_Erec_Rg_150C_O3 for i in Data_Fit_Rg]



#
plt.figure()
plt.plot(Data_Fit_Rg, Data_Rate_Erec_125C,"b*-")
plt.plot(Data_Fit_Rg, Data_Rate_Erec_150C,"ro-")
plt.grid()
plt.show()


plt.figure()
#Erec 125C
plt.plot(Data_Sample_Erec_Rg_Rg_125C, Data_Sample_Erec_Rg_Erec_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Erec_125C,label="Data_Fit_Erec_125C")
#Erec 150C
plt.plot(Data_Sample_Erec_Rg_Rg_150C, Data_Sample_Erec_Rg_Erec_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Erec_150C,label="Data_Fit_Erec_150C")
plt.grid()
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Erec_Rg_Rg_125C, Data_Sample_Erec_Rg_Erec_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Erec_125C,label="Data_Fit_Erec_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Erec_Rg_Rg_150C, Data_Sample_Erec_Rg_Erec_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Erec_150C,label="Data_Fit_Erec_150C")
plt.grid()
plt.legend()
plt.show()









