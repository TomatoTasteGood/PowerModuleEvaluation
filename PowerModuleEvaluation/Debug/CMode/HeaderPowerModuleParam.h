// 2019_12_24, hzc
//
//
#ifndef HEADER_POWERMODULE_PARAM_H_
#define HEADER_POWERMODULE_PARAM_H_

typedef struct{
    //loss
    double TEMP1;
    double TEMP2;
    double V_BASE;
    double P1_VCE_IC_TEMP1;
    double P2_VCE_IC_TEMP1;
    double P3_VCE_IC_TEMP1;
    double P1_VCE_IC_TEMP2;
    double P2_VCE_IC_TEMP2;
    double P3_VCE_IC_TEMP2;
    double P1_E_ON_TEMP1;
    double P2_E_ON_TEMP1;
    double P3_E_ON_TEMP1;
    double P1_E_ON_TEMP2;
    double P2_E_ON_TEMP2;
    double P3_E_ON_TEMP2;
    double P1_E_OFF_TEMP1; 
    double P2_E_OFF_TEMP1;
    double P3_E_OFF_TEMP1;
    double P1_E_OFF_TEMP2;
    double P2_E_OFF_TEMP2;
    double P3_E_OFF_TEMP2;
    double P1_VF_IF_TEMP1;
    double P2_VF_IF_TEMP1;
    double P3_VF_IF_TEMP1;
    double P1_VF_IF_TEMP2;
    double P2_VF_IF_TEMP2;
    double P3_VF_IF_TEMP2;
    double P1_E_REC_TEMP1;
    double P2_E_REC_TEMP1;
    double P3_E_REC_TEMP1;
    double P1_E_REC_TEMP2;
    double P2_E_REC_TEMP2;
    double P3_E_REC_TEMP2;
    double RG_ON_BASE;
    double RG_OFF_BASE;
    double P1_E_ON_RG;
    double P2_E_ON_RG;
    double P3_E_ON_RG;
    double P4_E_ON_RG;
    double P1_E_OFF_RG;
    double P2_E_OFF_RG;
    double P3_E_OFF_RG;
    double P4_E_OFF_RG;
    double P1_E_REC_RG;
    double P2_E_REC_RG;
    double P3_E_REC_RG;
    double P4_E_REC_RG;
    //themal
    //igbt
    double R_TH_IGBT_1;
    double T_TH_IGBT_1;
    double C_TH_IGBT_1;
    double R_TH_IGBT_2;
    double T_TH_IGBT_2;
    double C_TH_IGBT_2;
    double R_TH_IGBT_3;
    double T_TH_IGBT_3;
    double C_TH_IGBT_3;
    double R_TH_IGBT_4;
    double T_TH_IGBT_4;
    double C_TH_IGBT_4;
    double R_TH_IGBT_CH;
    double T_TH_IGBT_CH;
    double C_TH_IGBT_CH;
    //diode
    double R_TH_DIODE_1;
    double T_TH_DIODE_1;
    double C_TH_DIODE_1;
    double R_TH_DIODE_2;
    double T_TH_DIODE_2;
    double C_TH_DIODE_2;
    double R_TH_DIODE_3;
    double T_TH_DIODE_3;
    double C_TH_DIODE_3;
    double R_TH_DIODE_4;
    double T_TH_DIODE_4;
    double C_TH_DIODE_4;
    double R_TH_DIODE_CH;
    double T_TH_DIODE_CH;
    double C_TH_DIODE_CH;
    
}paramIGBT;

extern paramIGBT PARAM_IGBT_DATA[1];





#endif

