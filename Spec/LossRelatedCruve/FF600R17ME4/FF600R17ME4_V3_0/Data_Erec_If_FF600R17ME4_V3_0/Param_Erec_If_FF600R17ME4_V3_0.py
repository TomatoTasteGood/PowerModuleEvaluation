#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Erec_If_125C_O3 = 3.148e-08
p2_Erec_If_125C_O3 = -0.0001716
p3_Erec_If_125C_O3 = 0.2562
p4_Erec_If_125C_O3 =  43.56

p1_Erec_If_150C_O3 = 4.859e-08
p2_Erec_If_150C_O3 = -0.0002226
p3_Erec_If_150C_O3 = 0.3023
p4_Erec_If_150C_O3 = 50.93


#
Data_Sample_Erec_If_Erec_125C = [5.906643E+01,
6.768402E+01,
7.791741E+01,
8.797127E+01,
9.658887E+01,
1.053860E+02,
1.132855E+02,
1.204668E+02,
1.274686E+02,
1.330341E+02,
1.375224E+02,
1.418312E+02,
1.464991E+02,
1.506284E+02,
1.533214E+02,
1.556553E+02,
1.569120E+02,
1.581688E+02,
1.583483E+02,
1.585278E+02,
1.587074E+02,
1.590664E+02,
1.596050E+02
]
Data_Sample_Erec_If_If_125C = [6.075949E+01,
9.942463E+01,
1.505178E+02,
2.002301E+02,
2.485616E+02,
2.982739E+02,
3.507480E+02,
3.990794E+02,
4.543153E+02,
4.985040E+02,
5.509781E+02,
6.006904E+02,
6.531646E+02,
7.001151E+02,
7.539701E+02,
8.009206E+02,
8.520138E+02,
9.003452E+02,
9.528193E+02,
1.001151E+03,
1.053625E+03,
1.101956E+03,
1.195857E+03
]

Data_Sample_Erec_If_Erec_150C = [6.929982E+01,
7.863555E+01,
9.210054E+01,
1.021544E+02,
1.122083E+02,
1.215440E+02,
1.298025E+02,
1.391382E+02,
1.463196E+02,
1.527828E+02,
1.578097E+02,
1.626571E+02,
1.678636E+02,
1.718133E+02,
1.739677E+02,
1.755835E+02,
1.768402E+02,
1.775583E+02,
1.779174E+02,
1.780969E+02,
1.784560E+02,
1.789946E+02
]
Data_Sample_Erec_If_If_150C = [6.075949E+01,
9.666283E+01,
1.546605E+02,
1.988493E+02,
2.485616E+02,
2.955121E+02,
3.438435E+02,
3.976985E+02,
4.501726E+02,
4.957422E+02,
5.495972E+02,
6.006904E+02,
6.573072E+02,
7.014960E+02,
7.594937E+02,
8.009206E+02,
8.685846E+02,
9.031070E+02,
9.583429E+02,
1.001151E+03,
1.072957E+03,
1.172382E+03
]



#
Data_Fit_If = [i*10 for i in range(120)]
Data_Fit_Erec_125C = [p1_Erec_If_125C_O3*i**3+p2_Erec_If_125C_O3*i**2+p3_Erec_If_125C_O3*i+p4_Erec_If_125C_O3 for i in Data_Fit_If]
Data_Fit_Erec_150C = [p1_Erec_If_150C_O3*i**3+p2_Erec_If_150C_O3*i**2+p3_Erec_If_150C_O3*i+p4_Erec_If_150C_O3 for i in Data_Fit_If]

#
plt.figure()
#Erec 125C
plt.plot(Data_Sample_Erec_If_If_125C, Data_Sample_Erec_If_Erec_125C,"o")
plt.plot(Data_Fit_If, Data_Fit_Erec_125C,label="Data_Fit_Erec_125C")
#Erec 150C
plt.plot(Data_Sample_Erec_If_If_150C, Data_Sample_Erec_If_Erec_150C,"o")
plt.plot(Data_Fit_If, Data_Fit_Erec_150C,label="Data_Fit_Erec_150C")
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Erec_If_If_125C, Data_Sample_Erec_If_Erec_125C,"o")
plt.plot(Data_Fit_If, Data_Fit_Erec_125C,label="Data_Fit_Erec_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Erec_If_If_150C, Data_Sample_Erec_If_Erec_150C,"o")
plt.plot(Data_Fit_If, Data_Fit_Erec_150C,label="Data_Fit_Erec_150C")
plt.grid()
plt.legend()
plt.show()









