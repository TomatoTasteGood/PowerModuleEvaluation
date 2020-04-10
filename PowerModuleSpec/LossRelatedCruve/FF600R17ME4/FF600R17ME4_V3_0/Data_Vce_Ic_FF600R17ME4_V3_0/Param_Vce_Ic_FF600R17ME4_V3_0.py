#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Vce_Ic_125C_O3 = 1.357e-09
p2_Vce_Ic_125C_O3 = -2.665e-06 
p3_Vce_Ic_125C_O3 = 0.003954
p4_Vce_Ic_125C_O3 = 0.7529

p1_Vce_Ic_150C_O3 = 2.192e-09
p2_Vce_Ic_150C_O3 = -4.016e-06
p3_Vce_Ic_150C_O3 = 0.004587
p4_Vce_Ic_150C_O3 = 0.6725


#
Data_Sample_Vce_Ic_Vce_125C = [7.779056E-01,
9.758343E-01,
1.196778E+00,
1.445339E+00,
1.578826E+00,
1.744534E+00,
1.914845E+00,
2.085155E+00,
2.237054E+00,
2.347526E+00,
2.448792E+00,
2.545455E+00,
2.651323E+00,
2.775604E+00,
2.895282E+00,
3.005754E+00,
3.171461E+00,
3.332566E+00,
3.466053E+00,
3.581128E+00
]
Data_Sample_Vce_Ic_Ic_125C = [1.829596E+01,
5.381166E+01,
1.108520E+02,
1.947982E+02,
2.410762E+02,
3.034978E+02,
3.713004E+02,
4.434081E+02,
5.069058E+02,
5.553363E+02,
5.983857E+02,
6.414350E+02,
6.866368E+02,
7.404484E+02,
7.921076E+02,
8.383857E+02,
9.072646E+02,
9.729148E+02,
1.025650E+03,
1.070852E+03
]

Data_Sample_Vce_Ic_Vce_150C = [6.398159E-01,
8.469505E-01,
1.090909E+00,
1.233602E+00,
1.399310E+00,
1.569620E+00,
1.680092E+00,
1.790564E+00,
1.905639E+00,
2.006904E+00,
2.117376E+00,
2.223245E+00,
2.338320E+00,
2.448792E+00,
2.536249E+00,
2.669735E+00,
2.803222E+00,
2.927503E+00,
3.056387E+00,
3.199079E+00,
3.364787E+00
]
Data_Sample_Vce_Ic_Ic_150C = [9.686099E+00,
3.659193E+01,
8.717489E+01,
1.248430E+02,
1.775785E+02,
2.378475E+02,
2.787444E+02,
3.217937E+02,
3.669955E+02,
4.089686E+02,
4.563229E+02,
5.004484E+02,
5.510314E+02,
5.994619E+02,
6.371300E+02,
6.963229E+02,
7.533632E+02,
8.060987E+02,
8.599103E+02,
9.191031E+02,
9.858296E+02
]



#
Data_Fit_Ic = [i for i in range(1200)]
Data_Fit_Vce_125C = [p1_Vce_Ic_125C_O3*i**3+p2_Vce_Ic_125C_O3*i**2+p3_Vce_Ic_125C_O3*i+p4_Vce_Ic_125C_O3 for i in Data_Fit_Ic]
Data_Fit_Vce_150C = [p1_Vce_Ic_150C_O3*i**3+p2_Vce_Ic_150C_O3*i**2+p3_Vce_Ic_150C_O3*i+p4_Vce_Ic_150C_O3 for i in Data_Fit_Ic]

#
plt.figure()
#Erec 125C
plt.plot(Data_Sample_Vce_Ic_Ic_125C, Data_Sample_Vce_Ic_Vce_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Vce_125C,label="Data_Fit_Vce_125C")
#Erec 150C
plt.plot(Data_Sample_Vce_Ic_Ic_150C, Data_Sample_Vce_Ic_Vce_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Vce_150C,label="Data_Fit_Vce_150C")
plt.grid()
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Vce_Ic_Ic_125C, Data_Sample_Vce_Ic_Vce_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Vce_125C,label="Data_Fit_Vce_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Vce_Ic_Ic_150C, Data_Sample_Vce_Ic_Vce_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Vce_150C,label="Data_Fit_Vce_150C")
plt.grid()
plt.legend()
plt.show()









