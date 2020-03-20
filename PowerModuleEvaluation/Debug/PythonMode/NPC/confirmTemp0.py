# 2020_03_20, hzc
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
import PARAM_PAD
#
import calcModulation3LFuncs
import calcPowerLoss3LFuncs
import calcThermal3LFuncs
#
type_modulation = "SPWM"
type_IGBT = "FF600R17ME4"
type_Pad = "Test_3L"

v_dc = 925
freq_sw = 2000.0
freq_base = 10.0
i_base = 200.0
pf = -0.6
theta = np.arccos(pf)
index_m = 0.8
temp_input = 45.0


t_tot = PARAM_PAD.param[type_Pad]["T_TH_HEATSINK"]*9
t_sw = 1/freq_sw
num_sw_cycle_tot = int(t_tot/t_sw)

t1_T1 = 0
t2_T1 = 0
t3_T1 = 0
t4_T1 = 0
t5_T1 = 0
t6_T1 = 0
t7_T1 = temp_input
t1_D1 = 0
t2_D1 = 0
t3_D1 = 0
t4_D1 = 0
t5_D1 = 0
t6_D1 = 0
t7_D1 = temp_input
t1_T2 = 0
t2_T2 = 0
t3_T2 = 0
t4_T2 = 0
t5_T2 = 0
t6_T2 = 0
t7_T2 = temp_input
t1_D2 = 0
t2_D2 = 0
t3_D2 = 0
t4_D2 = 0
t5_D2 = 0
t6_D2 = 0
t7_D2 = temp_input
t1_T5 = 0
t2_T5 = 0
t3_T5 = 0
t4_T5 = 0
t5_T5 = 0
t6_T5 = 0
t7_T5 = temp_input
t1_D5 = 0
t2_D5 = 0
t3_D5 = 0
t4_D5 = 0
t5_D5 = 0
t6_D5 = 0
t7_D5 = temp_input

t7_T1_List = []
t7_T2_List = []
t7_T5_List = []
t7_D1_List = []
t7_D2_List = []
t7_D5_List = []

thermalList = [   [t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1], 
                  [t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1],
                  [t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2], 
                  [t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2],
                  [t1_T5, t2_T5, t3_T5, t4_T5, t5_T5, t6_T5, t7_T5], 
                  [t1_D5, t2_D5, t3_D5, t4_D5, t5_D5, t6_D5, t7_D5]]

for i in range(num_sw_cycle_tot):
    i_current = i_base*np.sqrt(2)*np.sin(freq_base*2*np.pi*i*t_sw)
    u_current = calcModulation3LFuncs.funcUCmdGenerator3L(t_sw*i, index_m, theta, freq_base, type_modulation)[0]                      
    eOut, tP, tZ, tN, mode = calcPowerLoss3LFuncs.funcPowerLossPerSwitch3L(i_current, u_current, v_dc, t_sw, thermalList[0][6], thermalList[1][6], thermalList[2][6], thermalList[3][6], thermalList[4][6], thermalList[5][6],[1,1],[1,1])
    pT1Tot = (eOut["e_on_T1"]+eOut["e_off_T1"]+eOut["e_cond_T1"])*freq_sw
    pD1Tot = (eOut["e_rec_D1"]+eOut["e_cond_D1"])*freq_sw
    pT2Tot = (eOut["e_on_T2"]+eOut["e_off_T2"]+eOut["e_cond_T2"])*freq_sw
    pD2Tot = (eOut["e_rec_D2"]+eOut["e_cond_D2"])*freq_sw
    pT5Tot = (eOut["e_on_T5"]+eOut["e_off_T5"]+eOut["e_cond_T5"])*freq_sw
    pD5Tot = (eOut["e_rec_D5"]+eOut["e_cond_D5"])*freq_sw
    # thermalList = [[t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1], 
    #               [t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2], 
    #               [t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1],
    #               [t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2],
    #               [t1_D5, t2_D5, t3_D5, t4_D5, t5_D5, t6_D5, t7_D5]]
    
    #print(thermalList[0])
    
    thermalList = calcThermal3LFuncs.funcThermal(pT1Tot, pD1Tot, pT2Tot, pD2Tot, pT5Tot, pD5Tot, t_sw, temp_input, thermalList)

    

    t7_T1_List.append(thermalList[0][6])
    t7_D1_List.append(thermalList[1][6])
    t7_T2_List.append(thermalList[2][6])
    t7_D2_List.append(thermalList[3][6])
    t7_T5_List.append(thermalList[4][6])
    t7_D5_List.append(thermalList[5][6])

plt.figure()
plt.subplot(3,1,1)
plt.plot(t7_T1_List,label="t7_T1")
plt.plot(t7_D1_List,label="t7_D1")
plt.legend()
plt.grid()

plt.subplot(3,1,2)
plt.plot(t7_T2_List,label="t7_T2")
plt.plot(t7_D2_List,label="t7_D2")
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(t7_T5_List,label="t7_T5")
plt.plot(t7_D5_List,label="t7_D5")
plt.legend()
plt.grid()
plt.show()







