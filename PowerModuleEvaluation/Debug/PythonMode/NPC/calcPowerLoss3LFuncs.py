# 2020_03_20, hzc
# 
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
#
import calcModulation3LFuncs
#
def funcPowerLossPerSwitch3L(i, u_cmd, v_dc, t_sw, temp_T1, temp_D1, temp_T2, temp_D2, temp_T5, temp_D5, rg_on, rg_off, dead_time=5e-6, npc_type=0, anpc_type=0, IGBT_type="FF600R17ME4"):
    if(npc_type==0):
        temp_T4 = temp_T1
        temp_D4 = temp_D1
        temp_T3 = temp_T2
        temp_D3 = temp_D2
        temp_T6 = temp_T5
        temp_D6 = temp_D5
        rg_on_T1 = rg_on[0]
        rg_off_T1 = rg_off[0]
        rg_on_T2 = rg_on[1]
        rg_off_T2 = rg_on[1]
        rg_on_T5 = rg_on[0]
        rg_off_T5 = rg_on[0]
        rg_on_T4 = rg_on_T1
        rg_off_T4 = rg_off_T1
        rg_on_T3 = rg_on_T2
        rg_off_T3 = rg_off_T2
        rg_on_T6 = rg_on_T5
        rg_off_T6 = rg_off_T5

    else:
        pass

    V_BASE = PARAM_IGBT.param[IGBT_type]["V_BASE"]
    TEMP1 = PARAM_IGBT.param[IGBT_type]["TEMP1"]
    TEMP2 = PARAM_IGBT.param[IGBT_type]["TEMP2"]
    RG_ON_BASE = PARAM_IGBT.param[IGBT_type]["RG_ON_BASE"]
    RG_OFF_BASE = PARAM_IGBT.param[IGBT_type]["RG_OFF_BASE"] 

    def paramCalc(temp_IGBT, temp_diode, rg_on, rg_off):
        p1_vce_ic = PARAM_IGBT.param[IGBT_type]["P1_VCE_IC_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P1_VCE_IC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P1_VCE_IC_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p2_vce_ic = PARAM_IGBT.param[IGBT_type]["P2_VCE_IC_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P2_VCE_IC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P2_VCE_IC_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p3_vce_ic = PARAM_IGBT.param[IGBT_type]["P3_VCE_IC_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P3_VCE_IC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P3_VCE_IC_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p4_vce_ic = PARAM_IGBT.param[IGBT_type]["P4_VCE_IC_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P4_VCE_IC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P4_VCE_IC_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        
        p1_e_on = PARAM_IGBT.param[IGBT_type]["P1_E_ON_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P1_E_ON_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P1_E_ON_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p2_e_on = PARAM_IGBT.param[IGBT_type]["P2_E_ON_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P2_E_ON_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P2_E_ON_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p3_e_on = PARAM_IGBT.param[IGBT_type]["P3_E_ON_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P3_E_ON_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P3_E_ON_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p4_e_on = PARAM_IGBT.param[IGBT_type]["P4_E_ON_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P4_E_ON_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P4_E_ON_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        
        p1_e_off = PARAM_IGBT.param[IGBT_type]["P1_E_OFF_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P1_E_OFF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P1_E_OFF_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p2_e_off = PARAM_IGBT.param[IGBT_type]["P2_E_OFF_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P2_E_OFF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P2_E_OFF_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p3_e_off = PARAM_IGBT.param[IGBT_type]["P3_E_OFF_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P3_E_OFF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P3_E_OFF_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        p4_e_off = PARAM_IGBT.param[IGBT_type]["P4_E_OFF_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P4_E_OFF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P4_E_OFF_TEMP1"])*(TEMP2-temp_IGBT)/(TEMP2-TEMP1)
        
        ratio_e_on_rg = PARAM_IGBT.param[IGBT_type]["P1_E_ON_RG"]*rg_on**3 + PARAM_IGBT.param[IGBT_type]["P2_E_ON_RG"]*rg_on**2 + PARAM_IGBT.param[IGBT_type]["P3_E_ON_RG"]*rg_on + PARAM_IGBT.param[IGBT_type]["P4_E_ON_RG"]
        ratio_e_off_rg = PARAM_IGBT.param[IGBT_type]["P1_E_OFF_RG"]*rg_off**3 + PARAM_IGBT.param[IGBT_type]["P2_E_OFF_RG"]*rg_off**2 + PARAM_IGBT.param[IGBT_type]["P3_E_OFF_RG"]*rg_off + PARAM_IGBT.param[IGBT_type]["P4_E_OFF_RG"]

        p1_vf_if = PARAM_IGBT.param[IGBT_type]["P1_VF_IF_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P1_VF_IF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P1_VF_IF_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p2_vf_if = PARAM_IGBT.param[IGBT_type]["P2_VF_IF_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P2_VF_IF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P2_VF_IF_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p3_vf_if = PARAM_IGBT.param[IGBT_type]["P3_VF_IF_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P3_VF_IF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P3_VF_IF_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p4_vf_if = PARAM_IGBT.param[IGBT_type]["P4_VF_IF_TEMP2"]-(PARAM_IGBT.param[IGBT_type]["P4_VF_IF_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P4_VF_IF_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)

        p1_e_rec = PARAM_IGBT.param[IGBT_type]["P1_E_REC_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P1_E_REC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P1_E_REC_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p2_e_rec = PARAM_IGBT.param[IGBT_type]["P2_E_REC_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P2_E_REC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P2_E_REC_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p3_e_rec = PARAM_IGBT.param[IGBT_type]["P3_E_REC_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P3_E_REC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P3_E_REC_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        p4_e_rec = PARAM_IGBT.param[IGBT_type]["P4_E_REC_TEMP2"] - (PARAM_IGBT.param[IGBT_type]["P4_E_REC_TEMP2"]-PARAM_IGBT.param[IGBT_type]["P4_E_REC_TEMP1"])*(TEMP2-temp_diode)/(TEMP2-TEMP1)
        
        ratio_e_rec_rg =  PARAM_IGBT.param[IGBT_type]["P1_E_REC_RG"]*rg_on**3 + PARAM_IGBT.param[IGBT_type]["P2_E_REC_RG"]*rg_on**2 + PARAM_IGBT.param[IGBT_type]["P3_E_REC_RG"]*rg_on + PARAM_IGBT.param[IGBT_type]["P4_E_REC_RG"]

        return [p1_vce_ic, p2_vce_ic, p3_vce_ic, p4_vce_ic, p1_e_on, p2_e_on, p3_e_on, p4_e_on, p1_e_off, p2_e_off, p3_e_off, p4_e_off, ratio_e_on_rg, ratio_e_off_rg], [p1_vf_if, p2_vf_if, p3_vf_if, p4_vf_if, p1_e_rec, p2_e_rec, p3_e_rec, p4_e_rec, ratio_e_rec_rg]

    [p1_vce_ic_T1, p2_vce_ic_T1, p3_vce_ic_T1, p4_vce_ic_T1, p1_e_on_T1, p2_e_on_T1, p3_e_on_T1, p4_e_on_T1, p1_e_off_T1, p2_e_off_T1, p3_e_off_T1, p4_e_off_T1, ratio_e_on_rg_T1, ratio_e_off_rg_T1], [p1_vf_if_D1, p2_vf_if_D1, p3_vf_if_D1, p4_vf_if_D1, p1_e_rec_D1, p2_e_rec_D1, p3_e_rec_D1, p4_e_rec_D1, ratio_e_rec_rg_D1] = paramCalc(temp_T1, temp_D1, rg_on_T1, rg_off_T1)
    [p1_vce_ic_T2, p2_vce_ic_T2, p3_vce_ic_T2, p4_vce_ic_T2, p1_e_on_T2, p2_e_on_T2, p3_e_on_T2, p4_e_on_T2, p1_e_off_T2, p2_e_off_T2, p3_e_off_T2, p4_e_off_T2, ratio_e_on_rg_T2, ratio_e_off_rg_T2], [p1_vf_if_D2, p2_vf_if_D2, p3_vf_if_D2, p4_vf_if_D2, p1_e_rec_D2, p2_e_rec_D2, p3_e_rec_D2, p4_e_rec_D2, ratio_e_rec_rg_D2] = paramCalc(temp_T2, temp_D2, rg_on_T2, rg_off_T2)
    [p1_vce_ic_T5, p2_vce_ic_T5, p3_vce_ic_T5, p4_vce_ic_T5, p1_e_on_T5, p2_e_on_T5, p3_e_on_T5, p4_e_on_T5, p1_e_off_T5, p2_e_off_T5, p3_e_off_T5, p4_e_off_T5, ratio_e_on_rg_T5, ratio_e_off_rg_T5], [p1_vf_if_D5, p2_vf_if_D5, p3_vf_if_D5, p4_vf_if_D5, p1_e_rec_D5, p2_e_rec_D5, p3_e_rec_D5, p4_e_rec_D5, ratio_e_rec_rg_D5] = paramCalc(temp_T5, temp_D5, rg_on_T5, rg_off_T5)
    [p1_vce_ic_T4, p2_vce_ic_T4, p3_vce_ic_T4, p4_vce_ic_T4, p1_e_on_T4, p2_e_on_T4, p3_e_on_T4, p4_e_on_T4, p1_e_off_T4, p2_e_off_T4, p3_e_off_T4, p4_e_off_T4, ratio_e_on_rg_T4, ratio_e_off_rg_T4], [p1_vf_if_D4, p2_vf_if_D4, p3_vf_if_D4, p4_vf_if_D4, p1_e_rec_D4, p2_e_rec_D4, p3_e_rec_D4, p4_e_rec_D4, ratio_e_rec_rg_D4] = paramCalc(temp_T4, temp_D4, rg_on_T4, rg_off_T4)
    [p1_vce_ic_T3, p2_vce_ic_T3, p3_vce_ic_T3, p4_vce_ic_T3, p1_e_on_T3, p2_e_on_T3, p3_e_on_T3, p4_e_on_T3, p1_e_off_T3, p2_e_off_T3, p3_e_off_T3, p4_e_off_T3, ratio_e_on_rg_T3, ratio_e_off_rg_T3], [p1_vf_if_D3, p2_vf_if_D3, p3_vf_if_D3, p4_vf_if_D3, p1_e_rec_D3, p2_e_rec_D3, p3_e_rec_D3, p4_e_rec_D3, ratio_e_rec_rg_D3] = paramCalc(temp_T3, temp_D3, rg_on_T3, rg_off_T3)
    [p1_vce_ic_T6, p2_vce_ic_T6, p3_vce_ic_T6, p4_vce_ic_T6, p1_e_on_T6, p2_e_on_T6, p3_e_on_T6, p4_e_on_T6, p1_e_off_T6, p2_e_off_T6, p3_e_off_T6, p4_e_off_T6, ratio_e_on_rg_T6, ratio_e_off_rg_T6], [p1_vf_if_D6, p2_vf_if_D6, p3_vf_if_D6, p4_vf_if_D6, p1_e_rec_D6, p2_e_rec_D6, p3_e_rec_D6, p4_e_rec_D6, ratio_e_rec_rg_D6] = paramCalc(temp_T6, temp_D6, rg_on_T6, rg_off_T6)
    #
    t_p = 0
    t_z = 0
    t_n = 0
    mode = 0
    if(u_cmd >0):
        t_p = u_cmd * t_sw
        t_z = (1-u_cmd)*t_sw
        t_n = 0
        mode = 1
    else:
        t_p = 0
        t_z = (u_cmd -(-1))*t_sw
        t_n = -u_cmd*t_sw
        mode = 0
    #
    e_loss_dict = {
        "e_on_T1":0.0, "e_off_T1":0.0, "e_cond_T1":0.0, "e_sw_T1":0.0,
        "e_on_T2":0.0, "e_off_T2":0.0, "e_cond_T2":0.0, "e_sw_T2":0.0,
        "e_on_T3":0.0, "e_off_T3":0.0, "e_cond_T3":0.0, "e_sw_T3":0.0,
        "e_on_T4":0.0, "e_off_T4":0.0, "e_cond_T4":0.0, "e_sw_T4":0.0,
        "e_on_T5":0.0, "e_off_T5":0.0, "e_cond_T5":0.0, "e_sw_T5":0.0,
        "e_on_T6":0.0, "e_off_T6":0.0, "e_cond_T6":0.0, "e_sw_T6":0.0,
                                       "e_cond_D1":0.0, "e_rec_D1":0.0,
                                       "e_cond_D2":0.0, "e_rec_D2":0.0,
                                       "e_cond_D3":0.0, "e_rec_D3":0.0,
                                       "e_cond_D4":0.0, "e_rec_D4":0.0,
                                       "e_cond_D5":0.0, "e_rec_D5":0.0,
                                       "e_cond_D6":0.0, "e_rec_D6":0.0
    }
    
    if(anpc_type == 0):
        if(i>=0):
            if(mode==1):
                if(t_p>dead_time and t_z>dead_time):
                    e_loss_dict["e_on_T1"] = (p1_e_on_T1*i**3 + p2_e_on_T1*i**2 + p3_e_on_T1*i + p4_e_on_T1)*(v_dc/V_BASE)*ratio_e_on_rg_T1
                    e_loss_dict["e_off_T1"] = (p1_e_off_T1*i**3 + p2_e_off_T1*i**2 + p3_e_off_T1*i + p4_e_off_T1)*(v_dc/V_BASE)*ratio_e_off_rg_T1
                    e_loss_dict["e_rec_D5"] = (p1_e_rec_D5*i**3 + p2_e_rec_D5*i**2 + p3_e_rec_D5*i + p4_e_rec_D5)*(v_dc/V_BASE)*ratio_e_rec_rg_D5
                e_loss_dict["e_cond_T1"] = (p1_vce_ic_T1*i**3 +p2_vce_ic_T1*i**2 + p3_vce_ic_T1*i + p4_vce_ic_T1)*i*t_p 
                e_loss_dict["e_cond_D5"] = (p1_vf_if_D5*i**3 +p2_vf_if_D5*i**2 + p3_vf_if_D5*i + p4_vf_if_D5)*i*t_z
                e_loss_dict["e_cond_T2"] = (p1_vce_ic_T2*i**3 +p2_vce_ic_T2*i**2 + p3_vce_ic_T2*i + p4_vce_ic_T2)*i*t_sw
            else:
                if(t_z>dead_time and t_n>dead_time):
                    e_loss_dict["e_on_T2"] = (p1_e_on_T2*i**3 + p2_e_on_T2*i**2 + p3_e_on_T2*i + p4_e_on_T2)*(v_dc/V_BASE)*ratio_e_on_rg_T2
                    e_loss_dict["e_off_T2"] = (p1_e_off_T2*i**3 + p2_e_off_T2*i**2 + p3_e_off_T2*i + p4_e_off_T2)*(v_dc/V_BASE)*ratio_e_off_rg_T2
                    e_loss_dict["e_rec_D4"] = (p1_e_rec_D4*i**3 + p2_e_rec_D4*i**2 + p3_e_rec_D4*i + p4_e_rec_D4)*(v_dc/V_BASE)*ratio_e_rec_rg_D4
                e_loss_dict["e_cond_T2"] = (p1_vce_ic_T2*i**3 + p2_vce_ic_T2*i**2 + p3_vce_ic_T2*i +p4_vce_ic_T2)*i*t_z
                e_loss_dict["e_cond_D5"] = (p1_vf_if_D2*i*i*i + p2_vf_if_D5*i*i + p3_vf_if_D5*i +p4_vf_if_D5)*i*t_z
                e_loss_dict["e_cond_D3"] = (p1_vf_if_D3*i*i*i + p2_vf_if_D3*i*i + p3_vf_if_D3*i +p4_vf_if_D3)*i*t_n
                e_loss_dict["e_cond_D4"] = (p1_vf_if_D4*i*i*i + p2_vf_if_D4*i*i + p3_vf_if_D4*i +p4_vf_if_D4)*i*t_n
        else:
            i = abs(i)
            if(mode==1):
                if(t_p>dead_time and t_z>dead_time):
                    e_loss_dict["e_on_T3"] = (p1_e_on_T3*i**3 + p2_e_on_T3*i**2 + p3_e_on_T3*i + p4_e_on_T3)*(v_dc/V_BASE)*ratio_e_on_rg_T3
                    e_loss_dict["e_off_T3"] = (p1_e_off_T3*i**3 + p2_e_off_T3*i**2 + p3_e_off_T3*i + p4_e_off_T3)*(v_dc/V_BASE)*ratio_e_off_rg_T3
                    e_loss_dict["e_rec_D1"] = (p1_e_rec_D1*i**3 + p2_e_rec_D1*i**2 + p3_e_rec_D1*i + p4_e_rec_D1)*(v_dc/V_BASE)*ratio_e_rec_rg_D1
                e_loss_dict["e_cond_D1"] = (p1_vf_if_D1*i**3 + p2_vf_if_D1*i**2 + p3_vf_if_D1*i + p4_vf_if_D1)*i*t_p
                e_loss_dict["e_cond_D2"] = (p1_vf_if_D2*i**3 + p2_vf_if_D2*i**2 + p3_vf_if_D2*i + p4_vf_if_D2)*i*t_p
                e_loss_dict["e_cond_D6"] = (p1_vf_if_D6*i**3 + p2_vf_if_D6*i**2 + p3_vf_if_D6*i + p4_vf_if_D6)*i*t_z
                e_loss_dict["e_cond_T3"] = (p1_vce_ic_T3*i**3 + p2_vce_ic_T3*i**2 + p3_vce_ic_T3*i + p3_vce_ic_T3)*i*t_sw
            else:
                if(t_z>dead_time and t_n>dead_time):
                    e_loss_dict["e_on_T4"] = (p1_e_on_T4*i**3 + p2_e_on_T4*i**2 + p3_e_on_T4*i + p4_e_on_T4)*(v_dc/V_BASE)*ratio_e_on_rg_T4
                    e_loss_dict["e_off_T4"] = (p1_e_off_T4*i**3 + p2_e_off_T4*i**2 + p3_e_off_T4*i + p4_e_off_T4)*(v_dc/V_BASE)*ratio_e_off_rg_T4
                    e_loss_dict["e_rec_D6"] = (p1_e_rec_D6*i**3 + p2_e_rec_D6*i**2 + p3_e_rec_D6*i + p4_e_rec_D6)*(v_dc/V_BASE)*(ratio_e_rec_rg_D6)
                e_loss_dict["e_cond_T3"] = (p1_vce_ic_T3*i**3 + p2_vce_ic_T3*i**2 + p3_vce_ic_T3*i + p4_vce_ic_T3)*i*t_sw
                e_loss_dict["e_cond_T4"] = (p1_vce_ic_T4*i**3 + p2_vce_ic_T4*i**2 + p3_vce_ic_T4*i + p4_vce_ic_T4)*i*t_n
                e_loss_dict["e_cond_D6"] = (p1_vf_if_D6*i**3 + p2_vf_if_D6*i**2 + p3_vf_if_D6*i + p4_vf_if_D6)*i*t_z

    return e_loss_dict, t_p, t_z, t_n, mode
    
#
if __name__ == "__main__":
    print(">"*50)
    print("I=600, U_CMD=0.5,Rg=1,Temp=125")
    e_out, t_p, t_z, t_n, mode = funcPowerLossPerSwitch3L(600, 0.5, 900, 500e-6, 125, 125, 125, 125, 125, 125, [1,1], [1,1])
    for i in e_out:
        print(i,' ---> ',e_out[i])


























