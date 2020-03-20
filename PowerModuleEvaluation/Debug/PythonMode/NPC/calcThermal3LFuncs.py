#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
import PARAM_PAD
#
def funcThermal(p_T1, p_D1, p_T2, p_D2, p_T5, p_D5, t_sample, temp_input, vars_list, type_solver="Euler1", type_IGBT="FF600R17ME4", type_pad="Test_3L"):
    thermal_T1_list, thermal_D1_list, thermal_T2_list, thermal_D2_list, thermal_T5_list, thermal_D5_list = vars_list
    t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1 = thermal_T1_list
    t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1 = thermal_D1_list
    t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2 = thermal_T2_list
    t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2 = thermal_D2_list
    t1_T5, t2_T5, t3_T5, t4_T5, t5_T5, t6_T5, t7_T5 = thermal_T5_list
    t1_D5, t2_D5, t3_D5, t4_D5, t5_D5, t6_D5, t7_D5 = thermal_D5_list
    if(type_solver == "Euler1"):
        # T1
        t1_T1 = t1_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT1"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t1_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"]* p_T1)
        t2_T1 = t2_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT2"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t2_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"]* p_T1)
        t3_T1 = t3_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT3"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t3_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"]* p_T1)
        t4_T1 = t4_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT4"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t4_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"]* p_T1)
        t5_T1 = t5_T1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"] * t5_T1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"]* p_T1)
        t6_T1 = t6_T1 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_T1 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_T1 = t1_T1 + t2_T1 + t3_T1 + t4_T1 + t5_T1 + t6_T1 + temp_input
        # D1
        t1_D1 = t1_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE1"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t1_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"]* p_D1)
        t2_D1 = t2_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE2"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t2_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"]* p_D1)
        t3_D1 = t3_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE3"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t3_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"]* p_D1)
        t4_D1 = t4_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE4"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t4_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"]* p_D1)
        t5_D1 = t5_D1 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"] * t5_D1 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"]* p_D1)
        t6_D1 = t6_D1 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_D1 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_D1 = t1_D1 + t2_D1 + t3_D1 + t4_D1 + t5_D1 + t6_D1 + temp_input
        # T2
        t1_T2 = t1_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT1"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t1_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"]* p_T2)
        t2_T2 = t2_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT2"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t2_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"]* p_T2)
        t3_T2 = t3_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT3"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t3_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"]* p_T2)
        t4_T2 = t4_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT4"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t4_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"]* p_T2)
        t5_T2 = t5_T2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"] * t5_T2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"]* p_T2)
        t6_T2 = t6_T2 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_T2 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_T2 = t1_T2 + t2_T2 + t3_T2 + t4_T2 + t5_T2 + t6_T2 + temp_input
        # D2
        t1_D2 = t1_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE1"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t1_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"]* p_D2)
        t2_D2 = t2_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE2"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t2_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"]* p_D2)
        t3_D2 = t3_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE3"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t3_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"]* p_D2)
        t4_D2 = t4_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE4"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t4_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"]* p_D2)
        t5_D2 = t5_D2 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"] * t5_D2 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"]* p_D2)
        t6_D2 = t6_D2 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_D2 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_D2 = t1_D2 + t2_D2 + t3_D2 + t4_D2 + t5_D2 + t6_D2 + temp_input
        # T5
        t1_T5 = t1_T5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT1"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t1_T5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"]* p_T5)
        t2_T5 = t2_T5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT2"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t2_T5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT2"]* p_T5)
        t3_T5 = t3_T5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT3"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t3_T5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT3"]* p_T5)
        t4_T5 = t4_T5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT4"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT1"] * t4_T5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT4"]* p_T5)
        t5_T5 = t5_T5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_IGBT_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"] * t5_T5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_IGBT_CH_BASE"]* p_T5)
        t6_T5 = t6_T5 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_T5 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_T5 = t1_T5 + t2_T5 + t3_T5 + t4_T5 + t5_T5 + t6_T5 + temp_input
        # D5
        t1_D5 = t1_D5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE1"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t1_D5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"]* p_D5)
        t2_D5 = t2_D5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE2"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t2_D5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE2"]* p_D5)
        t3_D5 = t3_D5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE3"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t3_D5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE3"]* p_D5)
        t4_D5 = t4_D5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE4"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE1"] * t4_D5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE4"]* p_D5)
        t5_D5 = t5_D5 + t_sample *(-1 / PARAM_IGBT.param[type_IGBT]["R_TH_DIODE_CH_BASE"] / PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"] * t5_D5 + 1/PARAM_IGBT.param[type_IGBT]["C_TH_DIODE_CH_BASE"]* p_D5)
        t6_D5 = t6_D5 + t_sample *(-1 / PARAM_PAD.param[type_pad]["R_TH_HEATSINK"] / PARAM_PAD.param[type_pad]["C_TH_HEATSINK"] * t6_D5 + 1/PARAM_PAD.param[type_pad]["C_TH_HEATSINK"]* (p_T1+p_D1+p_T2+p_D2+p_T5+p_D5))
        t7_D5 = t1_D5 + t2_D5 + t3_D5 + t4_D5 + t5_D5 + t6_D5 + temp_input
    return [[t1_T1, t2_T1, t3_T1, t4_T1, t5_T1, t6_T1, t7_T1],
            [t1_D1, t2_D1, t3_D1, t4_D1, t5_D1, t6_D1, t7_D1],
            [t1_T2, t2_T2, t3_T2, t4_T2, t5_T2, t6_T2, t7_T2],
            [t1_D2, t2_D2, t3_D2, t4_D2, t5_D2, t6_D2, t7_D2],
            [t1_T5, t2_T5, t3_T5, t4_T5, t5_T5, t6_T5, t7_T5],
            [t1_D5, t2_D5, t3_D5, t4_D5, t5_D5, t6_D5, t7_D5]]

#
if __name__ == "__main__":
    flagInit = 0
    tempOutlet = 35
    pLossT1List = []
    pLossT2List = []
    pLossT5List = []
    pLossD1List = []
    pLossD2List = []
    pLossD5List = []
    t1_T1_List = []
    t2_T1_List = []
    t3_T1_List = []
    t4_T1_List = []
    t5_T1_List = []
    t6_T1_List = []
    t7_T1_List = []
    t1_T2_List = []
    t2_T2_List = []
    t3_T2_List = []
    t4_T2_List = []
    t5_T2_List = []
    t6_T2_List = []
    t7_T2_List = []
    t1_T5_List = []
    t2_T5_List = []
    t3_T5_List = []
    t4_T5_List = []
    t5_T5_List = []
    t6_T5_List = []
    t7_T5_List = []
    t1_D1_List = []
    t2_D1_List = []
    t3_D1_List = []
    t4_D1_List = []
    t5_D1_List = []
    t6_D1_List = []
    t7_D1_List = []
    t1_D2_List = []
    t2_D2_List = []
    t3_D2_List = []
    t4_D2_List = []
    t5_D2_List = []
    t6_D2_List = []
    t7_D2_List = []
    t1_D5_List = []
    t2_D5_List = []
    t3_D5_List = []
    t4_D5_List = []
    t5_D5_List = []
    t6_D5_List = []
    t7_D5_List = []
    tList = []
    lastVarsList = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tempOutlet]]
    tSample = 500e-6
    pLossT1Peak = 1000*np.pi
    pLossD1Peak = 300*np.pi
    pLossT2Peak = 500*np.pi
    pLossD2Peak = 150*np.pi
    pLossT5Peak = 100*np.pi
    pLossD5Peak = 400*np.pi
    for i in range(int((45.0*0.1/tSample*1))):
        pLossT1 = pLossT1Peak*np.sin(2*np.pi*6*i*tSample)
        if(pLossT1<0):
            pLossT1=0
        pLossD1 = pLossD1Peak*np.sin(2*np.pi*6*i*tSample+np.pi)
        if(pLossD1<0):
            pLossD1=0
        pLossT2 = pLossT2Peak*np.sin(2*np.pi*6*i*tSample)
        if(pLossT2<0):
            pLossT2=0
        pLossD2 = pLossD2Peak*np.sin(2*np.pi*6*i*tSample+np.pi)
        if(pLossD2<0):
            pLossD2=0
        pLossT5 = pLossT5Peak*np.sin(2*np.pi*6*i*tSample)
        if(pLossT5<0):
            pLossT5=0
        pLossD5 = pLossD5Peak*np.sin(2*np.pi*6*i*tSample+np.pi)
        if(pLossD5<0):
            pLossD5=0
        lastVarsList = funcThermal(pLossT1, pLossD1, pLossT2, pLossD2, pLossT5, pLossD5, tSample, tempOutlet, lastVarsList)
        tList.append(i*tSample)
        pLossT1List.append(pLossT1)
        pLossT2List.append(pLossT2)
        pLossT5List.append(pLossT5)
        pLossD1List.append(pLossD1)
        pLossD2List.append(pLossD2)
        pLossD5List.append(pLossD5)
        t1_T1_List.append(lastVarsList[0][0])
        t2_T1_List.append(lastVarsList[0][1])
        t3_T1_List.append(lastVarsList[0][2])
        t4_T1_List.append(lastVarsList[0][3])
        t5_T1_List.append(lastVarsList[0][4])
        t6_T1_List.append(lastVarsList[0][5])
        t7_T1_List.append(lastVarsList[0][6])
        t1_T2_List.append(lastVarsList[2][0])
        t2_T2_List.append(lastVarsList[2][1])
        t3_T2_List.append(lastVarsList[2][2])
        t4_T2_List.append(lastVarsList[2][3])
        t5_T2_List.append(lastVarsList[2][4])
        t6_T2_List.append(lastVarsList[2][5])
        t7_T2_List.append(lastVarsList[2][6])
        t1_T5_List.append(lastVarsList[4][0])
        t2_T5_List.append(lastVarsList[4][1])
        t3_T5_List.append(lastVarsList[4][2])
        t4_T5_List.append(lastVarsList[4][3])
        t5_T5_List.append(lastVarsList[4][4])
        t6_T5_List.append(lastVarsList[4][5])
        t7_T5_List.append(lastVarsList[4][6])
        t1_D1_List.append(lastVarsList[1][0])
        t2_D1_List.append(lastVarsList[1][1])
        t3_D1_List.append(lastVarsList[1][2])
        t4_D1_List.append(lastVarsList[1][3])
        t5_D1_List.append(lastVarsList[1][4])
        t6_D1_List.append(lastVarsList[1][5])
        t7_D1_List.append(lastVarsList[1][6])
        t1_D2_List.append(lastVarsList[3][0])
        t2_D2_List.append(lastVarsList[3][1])
        t3_D2_List.append(lastVarsList[3][2])
        t4_D2_List.append(lastVarsList[3][3])
        t5_D2_List.append(lastVarsList[3][4])
        t6_D2_List.append(lastVarsList[3][5])
        t7_D2_List.append(lastVarsList[3][6])
        t1_D5_List.append(lastVarsList[5][0])
        t2_D5_List.append(lastVarsList[5][1])
        t3_D5_List.append(lastVarsList[5][2])
        t4_D5_List.append(lastVarsList[5][3])
        t5_D5_List.append(lastVarsList[5][4])
        t6_D5_List.append(lastVarsList[5][5])
        t7_D5_List.append(lastVarsList[5][6])
    
    # plt.figure()
    # plt.subplot(5,1,1)
    # plt.plot(tList, pLossT1List)
    # plt.grid()
    # plt.subplot(5,1,2)
    # plt.plot(tList, pLossD1List)
    # plt.grid()
    # plt.subplot(5,1,3)
    # plt.plot(tList, pLossT2List)
    # plt.grid()
    # plt.subplot(5,1,4)
    # plt.plot(tList, pLossD2List)
    # plt.grid()
    # plt.subplot(5,1,5)
    # plt.plot(tList, pLossD5List)
    # plt.grid()
    # plt.show()
    
    plt.figure()
    plt.subplot(7,1,1)
    plt.plot(tList, t1_T1_List)
    plt.grid()
    plt.subplot(7,1,2)
    plt.plot(tList, t2_T1_List)
    plt.grid()
    plt.subplot(7,1,3)
    plt.plot(tList, t3_T1_List)
    plt.grid()
    plt.subplot(7,1,4)
    plt.plot(tList, t4_T1_List)
    plt.grid()
    plt.subplot(7,1,5)
    plt.plot(tList, t5_T1_List)
    plt.grid()
    plt.subplot(7,1,6)
    plt.plot(tList, t6_T1_List)
    plt.grid()
    plt.subplot(7,1,7)
    plt.plot(tList, t7_T1_List)
    plt.grid()
    plt.show()
    
    # plt.figure()
    # plt.subplot(7,1,1)
    # plt.plot(tList, t1_D1_List)
    # plt.grid()
    # plt.subplot(7,1,2)
    # plt.plot(tList, t2_D1_List)
    # plt.grid()
    # plt.subplot(7,1,3)
    # plt.plot(tList, t3_D1_List)
    # plt.grid()
    # plt.subplot(7,1,4)
    # plt.plot(tList, t4_D1_List)
    # plt.grid()
    # plt.subplot(7,1,5)
    # plt.plot(tList, t5_D1_List)
    # plt.grid()
    # plt.subplot(7,1,6)
    # plt.plot(tList, t6_D1_List)
    # plt.grid()
    # plt.subplot(7,1,7)
    # plt.plot(tList, t7_D1_List)
    # plt.grid()
    # plt.show()

    # plt.figure()
    # plt.subplot(7,1,1)
    # plt.plot(tList, t1_T2_List)
    # plt.grid()
    # plt.subplot(7,1,2)
    # plt.plot(tList, t2_T2_List)
    # plt.grid()
    # plt.subplot(7,1,3)
    # plt.plot(tList, t3_T2_List)
    # plt.grid()
    # plt.subplot(7,1,4)
    # plt.plot(tList, t4_T2_List)
    # plt.grid()
    # plt.subplot(7,1,5)
    # plt.plot(tList, t5_T2_List)
    # plt.grid()
    # plt.subplot(7,1,6)
    # plt.plot(tList, t6_T2_List)
    # plt.grid()
    # plt.subplot(7,1,7)
    # plt.plot(tList, t7_T2_List)
    # plt.grid()
    # plt.show()
    
    # plt.figure()
    # plt.subplot(7,1,1)
    # plt.plot(tList, t1_D2_List)
    # plt.grid()
    # plt.subplot(7,1,2)
    # plt.plot(tList, t2_D2_List)
    # plt.grid()
    # plt.subplot(7,1,3)
    # plt.plot(tList, t3_D2_List)
    # plt.grid()
    # plt.subplot(7,1,4)
    # plt.plot(tList, t4_D2_List)
    # plt.grid()
    # plt.subplot(7,1,5)
    # plt.plot(tList, t5_D2_List)
    # plt.grid()
    # plt.subplot(7,1,6)
    # plt.plot(tList, t6_D2_List)
    # plt.grid()
    # plt.subplot(7,1,7)
    # plt.plot(tList, t7_D2_List)
    # plt.grid()
    # plt.show()

    plt.figure()
    plt.subplot(7,1,1)
    plt.plot(tList, t1_D5_List)
    plt.grid()
    plt.subplot(7,1,2)
    plt.plot(tList, t2_D5_List)
    plt.grid()
    plt.subplot(7,1,3)
    plt.plot(tList, t3_D5_List)
    plt.grid()
    plt.subplot(7,1,4)
    plt.plot(tList, t4_D5_List)
    plt.grid()
    plt.subplot(7,1,5)
    plt.plot(tList, t5_D5_List)
    plt.grid()
    plt.subplot(7,1,6)
    plt.plot(tList, t6_D5_List)
    plt.grid()
    plt.subplot(7,1,7)
    plt.plot(tList, t7_D5_List)
    plt.grid()
    plt.show()



