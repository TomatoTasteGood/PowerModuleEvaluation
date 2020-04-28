#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
import PARAM_IGBT

#
type = "FF600R17ME4"

current_list = np.linspace(50,600,12)

eon_IGBT_125C_list = [PARAM_IGBT.param[type]["P1_E_ON_TEMP1"]*i**3+PARAM_IGBT.param[type]["P2_E_ON_TEMP1"]*i**2+PARAM_IGBT.param[type]["P3_E_ON_TEMP1"]*i**1+PARAM_IGBT.param[type]["P4_E_ON_TEMP1"]*i**0 for i in current_list]
eon_IGBT_150C_list = [PARAM_IGBT.param[type]["P1_E_ON_TEMP2"]*i**3+PARAM_IGBT.param[type]["P2_E_ON_TEMP2"]*i**2+PARAM_IGBT.param[type]["P3_E_ON_TEMP2"]*i**1+PARAM_IGBT.param[type]["P4_E_ON_TEMP2"]*i**0 for i in current_list]

eoff_IGBT_125C_list = [PARAM_IGBT.param[type]["P1_E_OFF_TEMP1"]*i**3+PARAM_IGBT.param[type]["P2_E_OFF_TEMP1"]*i**2+PARAM_IGBT.param[type]["P3_E_OFF_TEMP1"]*i**1+PARAM_IGBT.param[type]["P4_E_OFF_TEMP1"]*i**0 for i in current_list]
eoff_IGBT_150C_list = [PARAM_IGBT.param[type]["P1_E_OFF_TEMP2"]*i**3+PARAM_IGBT.param[type]["P2_E_OFF_TEMP2"]*i**2+PARAM_IGBT.param[type]["P3_E_OFF_TEMP2"]*i**1+PARAM_IGBT.param[type]["P4_E_OFF_TEMP2"]*i**0 for i in current_list]

vce_IGBT_125C_list = [PARAM_IGBT.param[type]["P1_VCE_IC_TEMP1"]*i**3+PARAM_IGBT.param[type]["P2_VCE_IC_TEMP1"]*i**2+PARAM_IGBT.param[type]["P3_VCE_IC_TEMP1"]*i**1+PARAM_IGBT.param[type]["P4_VCE_IC_TEMP1"]*i**0 for i in current_list]
vce_IGBT_150C_list = [PARAM_IGBT.param[type]["P1_VCE_IC_TEMP2"]*i**3+PARAM_IGBT.param[type]["P2_VCE_IC_TEMP2"]*i**2+PARAM_IGBT.param[type]["P3_VCE_IC_TEMP2"]*i**1+PARAM_IGBT.param[type]["P4_VCE_IC_TEMP2"]*i**0 for i in current_list]


erec_diode_125C_list = [PARAM_IGBT.param[type]["P1_VF_IF_TEMP1"]*i**3+PARAM_IGBT.param[type]["P2_VF_IF_TEMP1"]*i**2+PARAM_IGBT.param[type]["P3_VF_IF_TEMP1"]*i**1+PARAM_IGBT.param[type]["P4_VF_IF_TEMP1"]*i**0 for i in current_list]
erec_diode_150C_list = [PARAM_IGBT.param[type]["P1_VF_IF_TEMP2"]*i**3+PARAM_IGBT.param[type]["P2_VF_IF_TEMP2"]*i**2+PARAM_IGBT.param[type]["P3_VF_IF_TEMP2"]*i**1+PARAM_IGBT.param[type]["P4_VF_IF_TEMP2"]*i**0 for i in current_list]

vf_diode_125C_list = [PARAM_IGBT.param[type]["P1_E_REC_TEMP1"]*i**3+PARAM_IGBT.param[type]["P2_E_REC_TEMP1"]*i**2+PARAM_IGBT.param[type]["P3_E_REC_TEMP1"]*i**1+PARAM_IGBT.param[type]["P4_E_REC_TEMP1"]*i**0 for i in current_list]
vf_diode_150C_list = [PARAM_IGBT.param[type]["P1_E_REC_TEMP2"]*i**3+PARAM_IGBT.param[type]["P2_E_REC_TEMP2"]*i**2+PARAM_IGBT.param[type]["P3_E_REC_TEMP2"]*i**1+PARAM_IGBT.param[type]["P4_E_REC_TEMP2"]*i**0 for i in current_list]

name_file = "curve_output.csv"
temp_file = open(name_file, "w")
for i in range(len(current_list)):
    temp_file.write(str(current_list[i]))
    temp_file.write(",")
temp_file.write("\n")
for i in range(len(current_list)):
    temp_file.write(str(eon_IGBT_125C_list[i]))
    temp_file.write(",")
temp_file.write("\n")
for i in range(len(current_list)):
    temp_file.write(str(eon_IGBT_150C_list[i]))
    temp_file.write(",")
temp_file.write("\n")
for i in range(len(current_list)):
    temp_file.write(str(eoff_IGBT_125C_list[i]))
    temp_file.write(",")
temp_file.write("\n")    
for i in range(len(current_list)):
    temp_file.write(str(eoff_IGBT_150C_list[i]))
    temp_file.write(",")
temp_file.write("\n")    
for i in range(len(current_list)):
    temp_file.write(str(vce_IGBT_125C_list[i]))
    temp_file.write(",")
temp_file.write("\n")    
for i in range(len(current_list)):
    temp_file.write(str(vce_IGBT_150C_list[i]))
    temp_file.write(",")
temp_file.write("\n")  
for i in range(len(current_list)):
    temp_file.write(str(erec_diode_125C_list[i]))
    temp_file.write(",")
temp_file.write("\n")     
for i in range(len(current_list)):
    temp_file.write(str(erec_diode_150C_list[i]))
    temp_file.write(",")
temp_file.write("\n")     
for i in range(len(current_list)):
    temp_file.write(str(vf_diode_125C_list[i]))
    temp_file.write(",")
temp_file.write("\n")       
for i in range(len(current_list)):
    temp_file.write(str(vf_diode_150C_list[i]))
    temp_file.write(",")
temp_file.write("\n")        

temp_file.close()    
    
    