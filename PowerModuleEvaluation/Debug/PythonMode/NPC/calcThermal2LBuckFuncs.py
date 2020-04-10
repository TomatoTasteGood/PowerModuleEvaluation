#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
import PARAM_PAD
#
def funcThermalBuck2L(p_T1, p_D1, p_T2, p_D2, t_sample, temp_input, vars_list, type_solver="Euler1", type_IGBT="FF600R17ME4", type_pad="Test_Buck_2L"):
    thermal_T1_list, thermal_D1_list, thermal_T2_list, thermal_D2_list = vars_list
    t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1 = thermal_T1_list
    t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1 = thermal_D1_list
    t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2 = thermal_T2_list
    t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2 = thermal_D2_list

    if(type_solver == "Euler1"):
        #T1
        t1_T1 = t1_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT1"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t1_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"]* p_T1)
        t2_T1 = t2_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT2"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"] * t2_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"]* p_T1)
        t3_T1 = t3_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT3"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"] * t3_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"]* p_T1)
        t4_T1 = t4_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT4"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"] * t4_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"]* p_T1)
        t5_T1 = t5_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"] * t5_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"]* p_T1)
        t6_T1 = t6_T1 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_T1 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D2))
        t7_T1 = t1_T1 + t2_T1 + t3_T1 + t4_T1 + t5_T1 + t6_T1 + temp_input
        
        #D1
        t1_D1 = t1_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE1"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t1_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"]* p_D1)
        t2_D1 = t2_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE2"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"] * t2_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"]* p_D1)
        t3_D1 = t3_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE3"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"] * t3_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"]* p_D1)
        t4_D1 = t4_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE4"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"] * t4_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"]* p_D1)
        t5_D1 = t5_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"] * t5_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"]* p_D1)
        t6_D1 = t6_D1 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_D1 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_D1+p_T2))
        t7_D1 = t1_D1 + t2_D1 + t3_D1 + t4_D1 + t5_D1 + t6_D1 + temp_input
        
        #T2
        t1_T2 = t1_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT1"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t1_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"]* p_T2)
        t2_T2 = t2_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT2"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"] * t2_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"]* p_T2)
        t3_T2 = t3_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT3"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"] * t3_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"]* p_T2)
        t4_T2 = t4_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT4"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"] * t4_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"]* p_T2)
        t5_T2 = t5_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"] * t5_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"]* p_T2)
        t6_T2 = t6_T2 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_T2 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T2+p_D2))
        t7_T2 = t1_T2 + t2_T2 + t3_T2 + t4_T2 + t5_T2 + t6_T2 + temp_input
        #D2
        t1_D2 = t1_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE1"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t1_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"]* p_D2)
        t2_D2 = t2_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE2"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"] * t2_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"]* p_D2)
        t3_D2 = t3_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE3"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"] * t3_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"]* p_D2)
        t4_D2 = t4_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE4"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"] * t4_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"]* p_D2)
        t5_D2 = t5_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"] * t5_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"]* p_D2)
        t6_D2 = t6_D2 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_D2 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D2))
        t7_D2 = t1_D2 + t2_D2 + t3_D2 + t4_D2 + t5_D2 + t6_D2 + temp_input

    
    return [[t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1],
            [t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1],
            [t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2],
            [t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2]]

#
if __name__ == "__main__":
    flag_init = 0
    temp_input = 35

