#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Eon_Ic_125C_O3 = 8.165e-07
p2_Eon_Ic_125C_O3 = -0.000837
p3_Eon_Ic_125C_O3 = 0.572
p4_Eon_Ic_125C_O3 = -8.963

p1_Eon_Ic_150C_O3 = 1.007e-06
p2_Eon_Ic_150C_O3 = -0.001025
p3_Eon_Ic_150C_O3 = 0.646
p4_Eon_Ic_150C_O3 = -9.889

p1_Eoff_Ic_125C_O3 = 4.654e-08
p2_Eoff_Ic_125C_O3 = -0.0001182
p3_Eoff_Ic_125C_O3 = 0.345
p4_Eoff_Ic_125C_O3 = 6.63

p1_Eoff_Ic_150C_O3 = 4.574e-08
p2_Eoff_Ic_150C_O3 = -0.000123
p3_Eoff_Ic_150C_O3 = 0.3788
p4_Eoff_Ic_150C_O3 = 11.3

#
Data_Sample_Eon_Ic_Eon_125C = [2.421525E+01,
4.125561E+01,
6.278027E+01,
7.892377E+01,
9.506726E+01,
1.094170E+02,
1.237668E+02,
1.381166E+02,
1.551570E+02,
1.695067E+02,
1.892377E+02,
2.080717E+02,
2.367713E+02,
2.609865E+02,
2.923767E+02,
3.291480E+02,
3.713004E+02,
4.188341E+02,
4.762332E+02,
5.327354E+02,
6.197309E+02,
6.995516E+02
]
Data_Sample_Eon_Ic_Ic_125C = [6.337543E+01,
1.005741E+02,
1.570608E+02,
1.997704E+02,
2.535017E+02,
3.003444E+02,
3.499426E+02,
4.009185E+02,
4.546498E+02,
5.001148E+02,
5.497130E+02,
5.993111E+02,
6.544202E+02,
6.998852E+02,
7.467279E+02,
7.990815E+02,
8.459242E+02,
8.982778E+02,
9.464983E+02,
9.933410E+02,
1.052583E+03,
1.103559E+03
]

Data_Sample_Eon_Ic_Eon_150C = [2.869955E+01,
5.560538E+01,
8.609865E+01,
1.076233E+02,
1.219731E+02,
1.372197E+02,
1.533632E+02,
1.730942E+02,
1.928251E+02,
2.143498E+02,
2.412556E+02,
2.690583E+02,
2.995516E+02,
3.354260E+02,
3.677130E+02,
4.179372E+02,
4.663677E+02,
5.372197E+02,
6.053812E+02,
7.040359E+02,
7.596413E+02,
8.143498E+02
]
Data_Sample_Eon_Ic_Ic_150C = [6.337543E+01,
1.267509E+02,
1.997704E+02,
2.645235E+02,
3.099885E+02,
3.595867E+02,
4.133180E+02,
4.725603E+02,
5.249139E+02,
5.758898E+02,
6.268657E+02,
6.750861E+02,
7.205511E+02,
7.646383E+02,
8.032147E+02,
8.500574E+02,
8.941447E+02,
9.451206E+02,
9.933410E+02,
1.048450E+03,
1.078760E+03,
1.107692E+03
]

Data_Sample_Eoff_Ic_Eoff_125C = [2.869955E+01,
5.022422E+01,
6.905830E+01,
8.699552E+01,
1.013453E+02,
1.183857E+02,
1.345291E+02,
1.470852E+02,
1.605381E+02,
1.757848E+02,
1.928251E+02,
2.080717E+02,
2.251121E+02,
2.403587E+02,
2.538117E+02,
2.708520E+02,
2.843049E+02,
3.004484E+02,
3.147982E+02
]
Data_Sample_Eoff_Ic_Ic_125C = [6.750861E+01,
1.295063E+02,
1.928817E+02,
2.521240E+02,
3.017222E+02,
3.623421E+02,
4.215844E+02,
4.684271E+02,
5.207807E+02,
5.800230E+02,
6.489093E+02,
7.067738E+02,
7.756602E+02,
8.390356E+02,
8.941447E+02,
9.616533E+02,
1.018140E+03,
1.081515E+03,
1.139380E+03
]

Data_Sample_Eoff_Ic_Eoff_150C = [3.497758E+01,
5.022422E+01,
7.623318E+01,
9.955157E+01,
1.147982E+02,
1.282511E+02,
1.417040E+02,
1.632287E+02,
1.766816E+02,
1.946188E+02,
2.107623E+02,
2.233184E+02,
2.358744E+02,
2.493274E+02,
2.654709E+02,
2.816143E+02,
2.977578E+02,
3.147982E+02,
3.318386E+02,
3.569507E+02
]
Data_Sample_Eoff_Ic_Ic_150C = [6.337543E+01,
1.074627E+02,
1.804822E+02,
2.521240E+02,
2.975890E+02,
3.416762E+02,
3.857635E+02,
4.587830E+02,
5.042480E+02,
5.662457E+02,
6.227325E+02,
6.695752E+02,
7.150402E+02,
7.618829E+02,
8.225029E+02,
8.845006E+02,
9.464983E+02,
1.007118E+03,
1.069116E+03,
1.161424E+03
]

#
Data_Fit_Ic = [i*10 for i in range(120)]
Data_Fit_Eon_125C = [p1_Eon_Ic_125C_O3*i**3+p2_Eon_Ic_125C_O3*i**2+p3_Eon_Ic_125C_O3*i+p4_Eon_Ic_125C_O3 for i in Data_Fit_Ic]
Data_Fit_Eon_150C = [p1_Eon_Ic_150C_O3*i**3+p2_Eon_Ic_150C_O3*i**2+p3_Eon_Ic_150C_O3*i+p4_Eon_Ic_150C_O3 for i in Data_Fit_Ic]
Data_Fit_Eoff_125C = [p1_Eoff_Ic_125C_O3*i**3+p2_Eoff_Ic_125C_O3*i**2+p3_Eoff_Ic_125C_O3*i+p4_Eoff_Ic_125C_O3 for i in Data_Fit_Ic]
Data_Fit_Eoff_150C = [p1_Eoff_Ic_150C_O3*i**3+p2_Eoff_Ic_150C_O3*i**2+p3_Eoff_Ic_150C_O3*i+p4_Eoff_Ic_150C_O3 for i in Data_Fit_Ic]


#
plt.figure()
#Eon 125C
plt.plot(Data_Sample_Eon_Ic_Ic_125C, Data_Sample_Eon_Ic_Eon_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eon_125C,label="Data_Fit_Eon_125C")
#Eon 150C
plt.plot(Data_Sample_Eon_Ic_Ic_150C, Data_Sample_Eon_Ic_Eon_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eon_150C,label="Data_Fit_Eon_150C")
#Eoff 125C
plt.plot(Data_Sample_Eoff_Ic_Ic_125C, Data_Sample_Eoff_Ic_Eoff_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eoff_125C,label="Data_Fit_Eoff_125C")
#Eoff 150C
plt.plot(Data_Sample_Eoff_Ic_Ic_150C, Data_Sample_Eoff_Ic_Eoff_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eoff_150C,label="Data_Fit_Eoff_150C")
plt.grid()
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Eon_Ic_Ic_125C, Data_Sample_Eon_Ic_Eon_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eon_125C,label="Data_Fit_Eon_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eon_Ic_Ic_150C, Data_Sample_Eon_Ic_Eon_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eon_150C,label="Data_Fit_Eon_150C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eoff_Ic_Ic_125C, Data_Sample_Eoff_Ic_Eoff_125C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eoff_125C,label="Data_Fit_Eoff_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eoff_Ic_Ic_150C, Data_Sample_Eoff_Ic_Eoff_150C,"o")
plt.plot(Data_Fit_Ic, Data_Fit_Eoff_150C,label="Data_Fit_Eoff_150C")
plt.grid()
plt.legend()
plt.show()












