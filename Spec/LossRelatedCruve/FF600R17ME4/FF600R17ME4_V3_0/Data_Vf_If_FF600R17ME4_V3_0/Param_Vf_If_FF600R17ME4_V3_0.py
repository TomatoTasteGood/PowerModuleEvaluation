#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_Vf_If_125C_O3 = 1.911e-09
p2_Vf_If_125C_O3 = -3.876e-06
p3_Vf_If_125C_O3 =  0.003766
p4_Vf_If_125C_O3 = 0.622

p1_Vf_If_150C_O3 =  1.603e-09
p2_Vf_If_150C_O3 = -3.469e-06
p3_Vf_If_150C_O3 = 0.00375
p4_Vf_If_150C_O3 = 0.6078


#
Data_Sample_Vf_If_Vf_125C = [6.130884E-01,
8.025258E-01,
9.954076E-01,
1.150402E+00,
1.305396E+00,
1.456946E+00,
1.556831E+00,
1.649828E+00,
1.739380E+00,
1.822044E+00,
1.908152E+00,
1.994259E+00,
2.056257E+00,
2.142365E+00,
2.235362E+00,
2.352468E+00
]
Data_Sample_Vf_If_If_125C = [1.614350E+01,
4.304933E+01,
9.578475E+01,
1.549776E+02,
2.249327E+02,
3.067265E+02,
3.659193E+02,
4.261883E+02,
4.875336E+02,
5.434978E+02,
6.080717E+02,
6.747982E+02,
7.221525E+02,
7.931839E+02,
8.695964E+02,
9.707623E+02
]

Data_Sample_Vf_If_Vf_150C = [6.234214E-01,
8.335247E-01,
1.002296E+00,
1.167623E+00,
1.312285E+00,
1.429392E+00,
1.570608E+00,
1.667049E+00,
1.777268E+00,
1.866820E+00,
1.952928E+00,
2.045924E+00,
2.132032E+00,
2.221584E+00,
2.314581E+00,
2.411022E+00,
2.497130E+00
]
Data_Sample_Vf_If_If_150C = [2.044843E+01,
5.704036E+01,
1.043946E+02,
1.646637E+02,
2.281614E+02,
2.873543E+02,
3.605381E+02,
4.175785E+02,
4.853812E+02,
5.434978E+02,
6.026906E+02,
6.683408E+02,
7.307623E+02,
7.985650E+02,
8.685202E+02,
9.449327E+02,
1.015964E+03
]



#
Data_Fit_If = [i for i in range(1200)]
Data_Fit_Vf_125C = [p1_Vf_If_125C_O3*i**3+p2_Vf_If_125C_O3*i**2+p3_Vf_If_125C_O3*i+p4_Vf_If_125C_O3 for i in Data_Fit_If]
Data_Fit_Vf_150C = [p1_Vf_If_150C_O3*i**3+p2_Vf_If_150C_O3*i**2+p3_Vf_If_150C_O3*i+p4_Vf_If_150C_O3 for i in Data_Fit_If]

#
plt.figure()
#Erec 125C
plt.plot(Data_Sample_Vf_If_If_125C, Data_Sample_Vf_If_Vf_125C,"o")
plt.plot(Data_Fit_If, Data_Fit_Vf_125C,label="Data_Fit_Vf_125C")
#Erec 150C
plt.plot(Data_Sample_Vf_If_If_150C, Data_Sample_Vf_If_Vf_150C,"o")
plt.plot(Data_Fit_If, Data_Fit_Vf_150C,label="Data_Fit_Vf_150C")
plt.grid()
plt.legend()
plt.show()


plt.figure()
plt.plot(Data_Sample_Vf_If_If_125C, Data_Sample_Vf_If_Vf_125C,"o")
plt.plot(Data_Fit_If, Data_Fit_Vf_125C,label="Data_Fit_Vf_125C")
plt.grid()
plt.legend()
plt.show()

plt.figure()
plt.plot(Data_Sample_Vf_If_If_150C, Data_Sample_Vf_If_Vf_150C,"o")
plt.plot(Data_Fit_If, Data_Fit_Vf_150C,label="Data_Fit_Vf_150C")
plt.grid()
plt.legend()
plt.show()









