// 2019_12_26, hzc
//
//
#include "HeaderConstParam.h"
#include "HeaderCalcPowerLossFuncs.h"
#include "HeaderPowerModuleParam.h"
//
#include "stdlib.h"
#include "math.h"
//
calcPowerLossFuncsOutput * funcPowerLossPerSwitch(calcPowerLossFuncsInput *p)
{
    double i;
    double uCmd;
    double tempIGBT;
    double tempDiode;
    double vDc;
    double tSw;
    double rGon;
    double rGoff;
    int typePowerModule;
    double deadTime;

    double eOnIGBT1 = 0.0;
    double eOffIGBT1 = 0.0;
    double eCondIGBT1 = 0.0;
    double eSwIGBT1 = 0.0;
    double eOnIGBT2 = 0.0;
    double eOffIGBT2 = 0.0;
    double eCondIGBT2 = 0.0;
    double eSwIGBT2 = 0.0;
    double eCondDiode1 = 0.0;
    double eRecDiode1 = 0.0;
    double eCondDiode2 = 0.0;
    double eRecDiode2 = 0.0;
    //
    double VBASE;
    double TEMP1;
    double TEMP2;
    double RG_ON_BASE;
    double RG_OFF_BASE;
    double p1VceIc;
    double p2VceIc;
    double p3VceIc;
    double p1EOn;
    double p2EOn;
    double p3EOn;
    double p1EOff;
    double p2EOff;
    double p3EOff;
    double p1VfIf;
    double p2VfIf;
    double p3VfIf;
    double p1ERec;
    double p2ERec;
    double p3ERec;
    double rateEOnRg;
    double rateEOffRg;
    double rateERecRg;

    

    // double p1EOnRg;
    // double p2EOnRg;
    // double p3EOnRg;
    // double p4EOnRg;
    // double p1EOffRg;
    // double p2EOffRg;
    // double p3EOffRg;
    // double p4EOffRg;
    // double p1ERecRg;
    // double p2ERecRg;
    // double p3ERecRg;
    // double p4ERecRg;
    double tOn;
    double tOff;
    calcPowerLossFuncsOutput *out = (calcPowerLossFuncsOutput *)calloc(1,sizeof(calcPowerLossFuncsOutput));
    // input
    i = p->i;
    uCmd = p->uCmd;
    tempIGBT = p->tempIGBT;
    tempDiode = p->tempDiode;
    vDc = p->vDc;
    tSw = p->tSw;
    rGon = p->rGon;
    rGoff = p->rGoff;

    typePowerModule = p->typePowerModule;
    deadTime = p->deadTime;
    VBASE = PARAM_IGBT_DATA[typePowerModule].V_BASE;
    TEMP1 = PARAM_IGBT_DATA[typePowerModule].TEMP1;
    TEMP2 = PARAM_IGBT_DATA[typePowerModule].TEMP2;
    p1VceIc = PARAM_IGBT_DATA[typePowerModule].P1_VCE_IC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P1_VCE_IC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P1_VCE_IC_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p2VceIc = PARAM_IGBT_DATA[typePowerModule].P2_VCE_IC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P2_VCE_IC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P2_VCE_IC_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p3VceIc = PARAM_IGBT_DATA[typePowerModule].P3_VCE_IC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P3_VCE_IC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P3_VCE_IC_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p1EOn = PARAM_IGBT_DATA[typePowerModule].P1_E_ON_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P1_E_ON_TEMP2-PARAM_IGBT_DATA[typePowerModule].P1_E_ON_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p2EOn = PARAM_IGBT_DATA[typePowerModule].P2_E_ON_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P2_E_ON_TEMP2-PARAM_IGBT_DATA[typePowerModule].P2_E_ON_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p3EOn = PARAM_IGBT_DATA[typePowerModule].P3_E_ON_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P3_E_ON_TEMP2-PARAM_IGBT_DATA[typePowerModule].P3_E_ON_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p1EOff = PARAM_IGBT_DATA[typePowerModule].P1_E_OFF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P1_E_OFF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P1_E_OFF_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p2EOff = PARAM_IGBT_DATA[typePowerModule].P2_E_OFF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P2_E_OFF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P2_E_OFF_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);
    p3EOff = PARAM_IGBT_DATA[typePowerModule].P3_E_OFF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P3_E_OFF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P3_E_OFF_TEMP1)*(TEMP2-tempIGBT)/(TEMP2-TEMP1);

    p1VfIf = PARAM_IGBT_DATA[typePowerModule].P1_VF_IF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P1_VF_IF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P1_VF_IF_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    p2VfIf = PARAM_IGBT_DATA[typePowerModule].P2_VF_IF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P2_VF_IF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P2_VF_IF_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    p3VfIf = PARAM_IGBT_DATA[typePowerModule].P3_VF_IF_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P3_VF_IF_TEMP2-PARAM_IGBT_DATA[typePowerModule].P3_VF_IF_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    p1ERec = PARAM_IGBT_DATA[typePowerModule].P1_E_REC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P1_E_REC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P1_E_REC_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    p2ERec = PARAM_IGBT_DATA[typePowerModule].P2_E_REC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P2_E_REC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P2_E_REC_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    p3ERec = PARAM_IGBT_DATA[typePowerModule].P3_E_REC_TEMP2-(PARAM_IGBT_DATA[typePowerModule].P3_E_REC_TEMP2-PARAM_IGBT_DATA[typePowerModule].P3_E_REC_TEMP1)*(TEMP2-tempDiode)/(TEMP2-TEMP1);
    
    rateEOnRg = PARAM_IGBT_DATA[typePowerModule].P1_E_ON_RG*rGon*rGon*rGon+PARAM_IGBT_DATA[typePowerModule].P2_E_ON_RG*rGon*rGon+PARAM_IGBT_DATA[typePowerModule].P3_E_ON_RG*rGon+PARAM_IGBT_DATA[typePowerModule].P4_E_ON_RG;
    rateEOffRg = PARAM_IGBT_DATA[typePowerModule].P1_E_OFF_RG*rGoff*rGoff*rGoff+PARAM_IGBT_DATA[typePowerModule].P2_E_OFF_RG*rGoff*rGoff+PARAM_IGBT_DATA[typePowerModule].P3_E_OFF_RG*rGoff+PARAM_IGBT_DATA[typePowerModule].P4_E_OFF_RG;
    rateERecRg = PARAM_IGBT_DATA[typePowerModule].P1_E_REC_RG*rGon*rGon*rGon+PARAM_IGBT_DATA[typePowerModule].P2_E_REC_RG*rGon*rGon+PARAM_IGBT_DATA[typePowerModule].P3_E_REC_RG*rGon+PARAM_IGBT_DATA[typePowerModule].P4_E_REC_RG;

    tOn = (uCmd-(-1))/2*tSw;
    tOff = (1-uCmd)/2*tSw;

    if(i>0)
    {
        if((tOn>deadTime)&&(tOff>deadTime))
        {
            eOnIGBT1 = (p1EOn*i*i+p2EOn*i+p3EOn)*(vDc/VBASE)*rateEOnRg;
            eOffIGBT1 = (p1EOff*i*i+p2EOff*i+p3EOff)*(vDc/VBASE)*rateEOffRg;
            eRecDiode2 = (p1ERec*i*i+p2ERec*i+p3ERec)*(vDc/VBASE)*rateERecRg;
        }
        eCondIGBT1 = (p1VceIc*i*i+p2VceIc*i+p3VceIc)*i*tOn;
        eCondDiode2 = (p1VfIf*i*i+p2VfIf*i+p3VfIf)*i*tOff;
        eSwIGBT1 = eOnIGBT1+eOffIGBT1;
    }
    else
    {
        i=fabs(i);
        if((tOn>deadTime)&&(tOff>deadTime))
        {
            eOnIGBT2 = (p1EOn*i*i+p2EOn*i+p3EOn)*(vDc/VBASE)*rateEOnRg;
            eOffIGBT2 = (p1EOff*i*i+p2EOff*i+p3EOff)*(vDc/VBASE)*rateEOffRg;
            eRecDiode1 = (p1ERec*i*i+p2ERec*i+p3ERec)*(vDc/VBASE)*rateERecRg;
        }
        eCondIGBT2 = (p1VceIc*i*i+p2VceIc*i+p3VceIc)*i*tOff;
        eCondDiode1 = (p1VfIf*i*i+p2VfIf*i+p3VfIf)*i*tOn;
        eSwIGBT2 = eOnIGBT1+eOffIGBT1;
    }
    // output
    out->eOnIGBT1 = eOnIGBT1;
    out->eOffIGBT1 = eOffIGBT1;
    out->eCondIGBT1 = eCondIGBT1;
    out->eSwIGBT1 = eSwIGBT1;
    out->eOnIGBT2 = eOnIGBT2;
    out->eOffIGBT2 = eOffIGBT2;
    out->eCondIGBT2 = eCondIGBT2;
    out->eSwIGBT2 = eSwIGBT2;
    out->eCondDiode1 = eCondDiode1;
    out->eRecDiode1 = eRecDiode1;
    out->eCondDiode2 = eCondDiode2;
    out->eRecDiode2 = eRecDiode2;

    return out;
}



