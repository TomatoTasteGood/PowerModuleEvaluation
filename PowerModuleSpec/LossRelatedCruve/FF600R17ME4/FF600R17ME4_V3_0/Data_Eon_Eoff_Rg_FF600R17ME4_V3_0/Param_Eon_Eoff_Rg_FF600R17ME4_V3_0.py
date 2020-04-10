#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Eon_Rg_125C_O3 = -0.193
p2_Eon_Rg_125C_O3 = 1.156
p3_Eon_Rg_125C_O3 = 53.47
p4_Eon_Rg_125C_O3 = 154.4

p1_Eon_Rg_150C_O3 = -0.2513
p2_Eon_Rg_150C_O3 = 1.928 
p3_Eon_Rg_150C_O3 = 53.18
p4_Eon_Rg_150C_O3 = 168.8

p1_Eoff_Rg_125C_O3 = -0.03427
p2_Eoff_Rg_125C_O3 = 0.8696 
p3_Eoff_Rg_125C_O3 = -3.644
p4_Eoff_Rg_125C_O3 = 183.2

p1_Eoff_Rg_150C_O3 = -0.01301
p2_Eoff_Rg_150C_O3 = 0.5199
p3_Eoff_Rg_150C_O3 = -2.416
p4_Eoff_Rg_150C_O3 = 205.9

p1_Rate_Eon_Rg_125C_O3 = -0.0009242
p2_Rate_Eon_Rg_125C_O3 = 0.005536
p3_Rate_Eon_Rg_125C_O3 = 0.256
p4_Rate_Eon_Rg_125C_O3 =  0.7393

p1_Rate_Eon_Rg_150C_O3 = -0.001124
p2_Rate_Eon_Rg_150C_O3 =  0.00862
p3_Rate_Eon_Rg_150C_O3 = 0.2378
p4_Rate_Eon_Rg_150C_O3 = 0.7547

p1_Rate_Eoff_Rg_125C_O3 = -0.00019
p2_Rate_Eoff_Rg_125C_O3 = 0.004821
p3_Rate_Eoff_Rg_125C_O3 = -0.0202
p4_Rate_Eoff_Rg_125C_O3 = 1.016

p1_Rate_Eoff_Rg_150C_O3 = -6.378e-05
p2_Rate_Eoff_Rg_150C_O3 = 0.002549
p3_Rate_Eoff_Rg_150C_O3 = -0.01184
p4_Rate_Eoff_Rg_150C_O3 = 1.009


#
Data_Sample_Eon_Rg_Eon_125C = [2.095067E+02,
2.367713E+02,
2.640359E+02,
2.920179E+02,
3.192825E+02,
3.486996E+02,
3.738117E+02,
4.025112E+02,
4.261883E+02,
4.527354E+02,
4.749776E+02,
4.993722E+02,
5.187444E+02,
5.409865E+02,
5.582063E+02,
5.761435E+02,
5.897758E+02,
6.005381E+02,
6.091480E+02,
6.184753E+02,
6.270852E+02
]
Data_Sample_Eon_Rg_Rg_125C = [1.011494E+00,
1.504598E+00,
1.985057E+00,
2.503448E+00,
2.983908E+00,
3.527586E+00,
3.995402E+00,
4.526437E+00,
4.994253E+00,
5.537931E+00,
5.993103E+00,
6.536782E+00,
7.004598E+00,
7.535632E+00,
8.003448E+00,
8.559770E+00,
9.002299E+00,
9.508046E+00,
9.988506E+00,
1.049425E+01,
1.094943E+01
]

Data_Sample_Eon_Rg_Eon_150C = [2.238565E+02,
2.539910E+02,
2.798206E+02,
3.056502E+02,
3.300448E+02,
3.608969E+02,
3.867265E+02,
3.989238E+02,
4.269058E+02,
4.477130E+02,
4.735426E+02,
4.972197E+02,
5.208969E+02,
5.431390E+02,
5.682511E+02,
5.861883E+02,
6.048430E+02,
6.199103E+02,
6.321076E+02,
6.400000E+02,
6.500448E+02
]
Data_Sample_Eon_Rg_Rg_150C = [1.011494E+00,
1.529885E+00,
1.985057E+00,
2.414943E+00,
2.844828E+00,
3.375862E+00,
3.831034E+00,
4.045977E+00,
4.551724E+00,
4.931034E+00,
5.424138E+00,
5.891954E+00,
6.372414E+00,
6.878161E+00,
7.447126E+00,
7.914943E+00,
8.445977E+00,
8.926437E+00,
9.520690E+00,
9.975862E+00,
1.054483E+01
]

Data_Sample_Eoff_Rg_Eoff_125C = [1.800897E+02,
1.793722E+02,
1.793722E+02,
1.793722E+02,
1.793722E+02,
1.793722E+02,
1.800897E+02,
1.815247E+02,
1.822422E+02,
1.836771E+02,
1.851121E+02,
1.872646E+02,
1.886996E+02,
1.908520E+02,
1.922870E+02,
1.937220E+02,
1.958744E+02,
1.973094E+02,
1.994619E+02,
2.008969E+02,
2.023318E+02
]
Data_Sample_Eoff_Rg_Rg_125C = [1.011494E+00,
1.504598E+00,
1.985057E+00,
2.541379E+00,
2.958621E+00,
3.514943E+00,
4.008046E+00,
4.640230E+00,
5.006897E+00,
5.537931E+00,
6.031034E+00,
6.637931E+00,
7.004598E+00,
7.573563E+00,
8.003448E+00,
8.534483E+00,
8.951724E+00,
9.457471E+00,
1.000115E+01,
1.040575E+01,
1.092414E+01
]

Data_Sample_Eoff_Rg_Eoff_150C = [2.037668E+02,
2.037668E+02,
2.030493E+02,
2.030493E+02,
2.030493E+02,
2.030493E+02,
2.037668E+02,
2.044843E+02,
2.052018E+02,
2.059193E+02,
2.073543E+02,
2.087892E+02,
2.102242E+02,
2.116592E+02,
2.130942E+02,
2.152466E+02,
2.166816E+02,
2.188341E+02,
2.209865E+02,
2.224215E+02,
2.245740E+02
]
Data_Sample_Eoff_Rg_Rg_150C = [1.011494E+00,
1.491954E+00,
2.010345E+00,
2.503448E+00,
2.958621E+00,
3.514943E+00,
3.957471E+00,
4.564368E+00,
4.994253E+00,
5.462069E+00,
6.031034E+00,
6.511494E+00,
6.979310E+00,
7.447126E+00,
8.003448E+00,
8.597701E+00,
9.052874E+00,
9.520690E+00,
9.975862E+00,
1.043103E+01,
1.091149E+01
]

#
Data_Fit_Rg = [i/10 for i in range(1,110)]
Data_Fit_Eon_125C = [p1_Eon_Rg_125C_O3*i**3+p2_Eon_Rg_125C_O3*i**2+p3_Eon_Rg_125C_O3*i+p4_Eon_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Fit_Eon_150C = [p1_Eon_Rg_150C_O3*i**3+p2_Eon_Rg_150C_O3*i**2+p3_Eon_Rg_150C_O3*i+p4_Eon_Rg_150C_O3 for i in Data_Fit_Rg]
Data_Fit_Eoff_125C = [p1_Eoff_Rg_125C_O3*i**3+p2_Eoff_Rg_125C_O3*i**2+p3_Eoff_Rg_125C_O3*i+p4_Eoff_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Fit_Eoff_150C = [p1_Eoff_Rg_150C_O3*i**3+p2_Eoff_Rg_150C_O3*i**2+p3_Eoff_Rg_150C_O3*i+p4_Eoff_Rg_150C_O3 for i in Data_Fit_Rg]

Data_Rate_Eon_125C = [p1_Rate_Eon_Rg_125C_O3*i**3+p2_Rate_Eon_Rg_125C_O3*i**2+p3_Rate_Eon_Rg_125C_O3*i+p4_Rate_Eon_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Rate_Eon_150C = [p1_Rate_Eon_Rg_150C_O3*i**3+p2_Rate_Eon_Rg_150C_O3*i**2+p3_Rate_Eon_Rg_150C_O3*i+p4_Rate_Eon_Rg_150C_O3 for i in Data_Fit_Rg]

Data_Rate_Eoff_125C = [p1_Rate_Eoff_Rg_125C_O3*i**3+p2_Rate_Eoff_Rg_125C_O3*i**2+p3_Rate_Eoff_Rg_125C_O3*i+p4_Rate_Eoff_Rg_125C_O3 for i in Data_Fit_Rg]
Data_Rate_Eoff_150C = [p1_Rate_Eoff_Rg_150C_O3*i**3+p2_Rate_Eoff_Rg_150C_O3*i**2+p3_Rate_Eoff_Rg_150C_O3*i+p4_Rate_Eoff_Rg_150C_O3 for i in Data_Fit_Rg]

#
plt.figure()
plt.plot(Data_Fit_Rg,Data_Rate_Eon_125C,"b*-",label="Data_Rate_Eon_125C")
plt.plot(Data_Fit_Rg,Data_Rate_Eon_150C,"ro-",label="Data_Rate_Eon_150C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Fit_Rg,Data_Rate_Eoff_125C,"b*-",label="Data_Rate_Eoff_125C")
plt.plot(Data_Fit_Rg,Data_Rate_Eoff_150C,"ro-",label="Data_Rate_Eoff_150C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
#Eon 125C
plt.plot(Data_Sample_Eon_Rg_Rg_125C, Data_Sample_Eon_Rg_Eon_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eon_125C,label="Data_Fit_Eon_125C")
#Eon 150C
plt.plot(Data_Sample_Eon_Rg_Rg_150C, Data_Sample_Eon_Rg_Eon_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eon_150C,label="Data_Fit_Eon_150C")
#Eoff 125C
plt.plot(Data_Sample_Eoff_Rg_Rg_125C, Data_Sample_Eoff_Rg_Eoff_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eoff_125C,label="Data_Fit_Eoff_125C")
#Eoff 150C
plt.plot(Data_Sample_Eoff_Rg_Rg_150C, Data_Sample_Eoff_Rg_Eoff_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eoff_150C,label="Data_Fit_Eoff_150C")
plt.grid()
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Eon_Rg_Rg_125C, Data_Sample_Eon_Rg_Eon_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eon_125C,label="Data_Fit_Eon_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eon_Rg_Rg_150C, Data_Sample_Eon_Rg_Eon_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eon_150C,label="Data_Fit_Eon_150C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eoff_Rg_Rg_125C, Data_Sample_Eoff_Rg_Eoff_125C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eoff_125C,label="Data_Fit_Eoff_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Eoff_Rg_Rg_150C, Data_Sample_Eoff_Rg_Eoff_150C,"o")
plt.plot(Data_Fit_Rg, Data_Fit_Eoff_150C,label="Data_Fit_Eoff_150C")
plt.grid()
plt.legend()
plt.show()












