#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
import PARAM_PAD
#
import calcPowerLoss2LBuckFuncs
import calcThermal2LBuckFuncs
#

type_IGBT = "FF600R17ME4"
type_pad = "Test_Buck_2L"

v_dc = 900
freq_sw = 2000.0
i_base = 200.0
temp_input = 45

t_tot = PARAM_PAD.param[type_pad]["T_TH_HEATSINK"]*9
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

t7_T1_list = []
t7_D1_list = []
t7_T2_list = []
t7_D2_list = []

p_T1_tot = 0
p_D1_tot = 0
p_T2_tot = 0
p_D2_tot = 0


p_T1_tot_list = []
p_D1_Tot_list = []
p_T2_tot_list = []
p_D2_tot_list = []

thermalList = [   [t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1], 
                  [t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1],
                  [t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2], 
                  [t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2]]

for i in range(num_sw_cycle_tot):
    i_current= i_base
    e_out, t_p, t_n = calcPowerLoss2LBuckFuncs.funcPowerLossPerSwitchBucK2L(i_current, 0, v_dc, t_sw, t7_T1, t7_D1, t7_T2, t7_D2, [4], [4])
    p_T1_tot = (e_out["e_on_T1"]+e_out["e_off_T1"]+e_out["e_cond_T1"])*freq_sw
    p_D1_tot = (e_out["e_rec_D1"]+e_out["e_cond_D1"])*freq_sw
    p_T2_tot = (e_out["e_on_T2"]+e_out["e_off_T2"]+e_out["e_cond_T2"])*freq_sw
    p_D2_Tot = (e_out["e_rec_D2"]+e_out["e_cond_D2"])*freq_sw
    p_T1_tot_list.append(p_T1_tot)
    p_D1_Tot_list.append(p_D1_tot)
    p_T2_tot_list.append(p_T2_tot)
    p_D2_tot_list.append(p_D2_tot)
    thermalList = calcThermal2LBuckFuncs.funcThermalBuck2L(p_T1_tot, p_D1_tot, p_T2_tot, p_D2_tot, t_sw, temp_input, thermalList)
    t7_T1_list.append(thermalList[0][6])
    t7_D1_list.append(thermalList[1][6])
    t7_T2_list.append(thermalList[2][6])
    t7_D2_list.append(thermalList[3][6])

plt.figure()
plt.plot(t7_T1_list,label="T1")
plt.plot(t7_D1_list,label="D1")
plt.plot(t7_T2_list,label="T2")
plt.plot(t7_D2_list,label="D2")
plt.legend()
plt.grid()
plt.show()
