#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT
#

#
def funcPowerLossPerSwitchBucK2L(i, u_cmd, v_dc, t_sw, temp_T1, temp_D1, temp_T2, temp_D2, rg_on_list, rg_off_list, dead_time=5e-6, IGBT_type="FF600R17ME4"):
    rg_on_T1 = rg_on_list[0] 
    rg_off_T1 = rg_off_list[0]
    rg_on_T2 = rg_on_T1
    rg_off_T2 = rg_off_T1
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
    
    #
    t_p = (u_cmd-(-1))*t_sw/2.0
    t_n = (1-u_cmd)*t_sw/2.0
    #
    e_loss_dict = {
        "e_on_T1":0.0, "e_off_T1":0.0, "e_cond_T1":0.0, "e_sw_T1":0.0,
        "e_on_T2":0.0, "e_off_T2":0.0, "e_cond_T2":0.0, "e_sw_T2":0.0,
                                       "e_cond_D1":0.0, "e_rec_D1":0.0,
                                       "e_cond_D2":0.0, "e_rec_D2":0.0
    }

    if(i>=0):
        if(t_p>dead_time and t_n>dead_time):
            e_loss_dict["e_on_T1"] = (p1_e_on_T1*i**3 + p2_e_on_T1*i**2 + p3_e_on_T1*i + p4_e_on_T1)*(v_dc/V_BASE)*ratio_e_on_rg_T1
            e_loss_dict["e_off_T1"] = (p1_e_off_T1*i**3 + p2_e_off_T1*i**2 + p3_e_off_T1*i + p4_e_off_T1)*(v_dc/V_BASE)*ratio_e_off_rg_T1
            e_loss_dict["e_rec_D2"] = (p1_e_rec_D2*i**3 + p2_e_rec_D2*i**2 + p3_e_rec_D2*i + p4_e_rec_D2)*(v_dc/V_BASE)*ratio_e_rec_rg_D2
        e_loss_dict["e_cond_T1"] = (p1_vce_ic_T1*i**3 +p2_vce_ic_T1*i**2 + p3_vce_ic_T1*i + p4_vce_ic_T1)*i*t_p 
        e_loss_dict["e_cond_D2"] = (p1_vf_if_D2*i**3 +p2_vf_if_D2*i**2 + p3_vf_if_D2*i + p4_vf_if_D2)*i*t_n
    else:
        i = abs(i)
        if(t_p>dead_time and t_n>dead_time):
            e_loss_dict["e_on_T2"] = (p1_e_on_T2*i**3 + p2_e_on_T2*i**2 + p3_e_on_T2*i + p4_e_on_T2)*(v_dc/V_BASE)*ratio_e_on_rg_T2
            e_loss_dict["e_off_T2"] = (p1_e_off_T2*i**3 + p2_e_off_T2*i**2 + p3_e_off_T2*i + p4_e_off_T2)*(v_dc/V_BASE)*ratio_e_off_rg_T2
            e_loss_dict["e_rec_D1"] = (p1_e_rec_D1*i**3 + p2_e_rec_D1*i**2 + p3_e_rec_D1*i + p4_e_rec_D1)*(v_dc/V_BASE)*ratio_e_rec_rg_D1
        e_loss_dict["e_cond_T2"] = (p1_vce_ic_T2*i**3 +p2_vce_ic_T2*i**2 + p3_vce_ic_T2*i + p4_vce_ic_T2)*i*t_p 
        e_loss_dict["e_cond_D1"] = (p1_vf_if_D1*i**3 +p2_vf_if_D1*i**2 + p3_vf_if_D1*i + p4_vf_if_D1)*i*t_n
    
    return e_loss_dict, t_p, t_n


#
if __name__ == "__main__":
    print(">"*50)
    print("")
    e_out, t_p, t_n = funcPowerLossPerSwitchBucK2L(600, 0, 900, 500e-6, 125, 125, 125, 125, [4], [4])
    for i in e_out:
        print(i, '--->', e_out[i], "loss: ",e_out[i]*2000)