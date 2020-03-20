// 2019_12_24, hzc
//
//
#include "HeaderConstParam.h"
#include "HeaderCalcThermalFuncs.h"
#include "HeaderPadParam.h"
#include "HeaderPowerModuleParam.h"
//
#include "stdlib.h"
#include "math.h"
//
calcThermalFuncsOutput * funcThermal(calcThermalFuncsInput *p)
{
    //
    double powerLossIGBT;
    double powerLossDiode;
    double tSample;
    double tempAmbient;
    double y1;
    double y2;
    double y3;
    double y4;
    double y5;
    double y6;
    double y7;
    double z1;
    double z2;
    double z3;
    double z4;
    double z5;
    double z6;
    double z7;
    int typePowerModule;
    int typePad;
    int typeSolver;

    double rthIGBT1;
    double rthIGBT2;
    double rthIGBT3;
    double rthIGBT4;
    double rthIGBTCh;
    double cthIGBT1;
    double cthIGBT2;
    double cthIGBT3;
    double cthIGBT4;
    double cthIGBTCh;
    double rthDiode1;
    double rthDiode2;
    double rthDiode3;
    double rthDiode4;
    double rthDiodeCh;
    double cthDiode1;
    double cthDiode2;
    double cthDiode3;
    double cthDiode4;
    double cthDiodeCh;
    double rthPad;
    double cthPad;

    calcThermalFuncsOutput *out = (calcThermalFuncsOutput *)calloc(1, sizeof(calcThermalFuncsOutput));
    // input 
    powerLossIGBT = p->powerLossIGBT;
    powerLossDiode = p->powerLossDiode;
    tSample = p->tSample;
    tempAmbient = p->tempAmbient;
    y1 = p->lastThermalVars.y1;
    y2 = p->lastThermalVars.y2;
    y3 = p->lastThermalVars.y3;
    y4 = p->lastThermalVars.y4;
    y5 = p->lastThermalVars.y5;
    y6 = p->lastThermalVars.y6;
    y7 = p->lastThermalVars.y7;
    z1 = p->lastThermalVars.z1;
    z2 = p->lastThermalVars.z2;
    z3 = p->lastThermalVars.z3;
    z4 = p->lastThermalVars.z4;
    z5 = p->lastThermalVars.z5;
    z6 = p->lastThermalVars.z6;
    z7 = p->lastThermalVars.z7;
    typePowerModule =p->typePowerModule;
    typePad = p->typePad;
    typeSolver = p->typeSolver;
    rthIGBT1 = PARAM_IGBT_DATA[typePowerModule].R_TH_IGBT_1;
    rthIGBT2 = PARAM_IGBT_DATA[typePowerModule].R_TH_IGBT_2;
    rthIGBT3 = PARAM_IGBT_DATA[typePowerModule].R_TH_IGBT_3;
    rthIGBT4 = PARAM_IGBT_DATA[typePowerModule].R_TH_IGBT_4;
    rthIGBTCh = PARAM_IGBT_DATA[typePowerModule].R_TH_IGBT_CH;
    cthIGBT1 = PARAM_IGBT_DATA[typePowerModule].C_TH_IGBT_1;
    cthIGBT2 = PARAM_IGBT_DATA[typePowerModule].C_TH_IGBT_2;
    cthIGBT3 = PARAM_IGBT_DATA[typePowerModule].C_TH_IGBT_3;
    cthIGBT4 = PARAM_IGBT_DATA[typePowerModule].C_TH_IGBT_4;
    cthIGBTCh = PARAM_IGBT_DATA[typePowerModule].C_TH_IGBT_CH;
    rthDiode1 = PARAM_IGBT_DATA[typePowerModule].R_TH_DIODE_1;
    rthDiode2 = PARAM_IGBT_DATA[typePowerModule].R_TH_DIODE_2;
    rthDiode3 = PARAM_IGBT_DATA[typePowerModule].R_TH_DIODE_3;
    rthDiode4 = PARAM_IGBT_DATA[typePowerModule].R_TH_DIODE_4;
    rthDiodeCh = PARAM_IGBT_DATA[typePowerModule].R_TH_DIODE_CH;
    cthDiode1 = PARAM_IGBT_DATA[typePowerModule].C_TH_DIODE_1;
    cthDiode2 = PARAM_IGBT_DATA[typePowerModule].C_TH_DIODE_2;
    cthDiode3 = PARAM_IGBT_DATA[typePowerModule].C_TH_DIODE_3;
    cthDiode4 = PARAM_IGBT_DATA[typePowerModule].C_TH_DIODE_4;
    cthDiodeCh = PARAM_IGBT_DATA[typePowerModule].C_TH_DIODE_CH;
    rthPad = RTH_PAD_DATA[typePad].R_TH;
    cthPad = RTH_PAD_DATA[typePad].C_TH;
    //
    if(typeSolver == 0)
    {
        y1 = y1+tSample*(-1.0/rthIGBT1/cthIGBT1*y1+1.0/cthIGBT1*powerLossIGBT);
        y2 = y2+tSample*(-1.0/rthIGBT2/cthIGBT2*y2+1.0/cthIGBT2*powerLossIGBT);
        y3 = y3+tSample*(-1.0/rthIGBT3/cthIGBT3*y3+1.0/cthIGBT3*powerLossIGBT);
        y4 = y4+tSample*(-1.0/rthIGBT4/cthIGBT4*y4+1.0/cthIGBT4*powerLossIGBT);
        y5 = y5+tSample*(-1.0/rthIGBTCh/cthIGBTCh*y5+1.0/cthIGBTCh*powerLossIGBT);
        y6 = y6+tSample*(-1.0/rthPad/cthPad*y6+1.0/cthPad*(powerLossIGBT+powerLossDiode));
        y7 = y1+y2+y3+y4+y5+y6+tempAmbient;
        z1 = z1+tSample*(-1.0/rthDiode1/cthDiode1*z1+1.0/cthDiode1*powerLossDiode);
        z2 = z2+tSample*(-1.0/rthDiode2/cthDiode2*z2+1.0/cthDiode2*powerLossDiode);
        z3 = z3+tSample*(-1.0/rthDiode3/cthDiode3*z3+1.0/cthDiode3*powerLossDiode);
        z4 = z4+tSample*(-1.0/rthDiode4/cthDiode4*z4+1.0/cthDiode4*powerLossDiode);
        z5 = z5+tSample*(-1.0/rthDiodeCh/cthDiodeCh*z5+1.0/cthDiodeCh*powerLossDiode);
        z6 = z6+tSample*(-1.0/rthPad/cthPad*z6+1.0/cthPad*(powerLossIGBT+powerLossDiode));
        z7 = z1+z2+z3+z4+z5+z6+tempAmbient;
    }
    
    // output
    out->outputThermalVars.y1 = y1;
    out->outputThermalVars.y2 = y2;
    out->outputThermalVars.y3 = y3;
    out->outputThermalVars.y4 = y4;
    out->outputThermalVars.y5 = y5;
    out->outputThermalVars.y6 = y6;
    out->outputThermalVars.y7 = y7;
    out->outputThermalVars.z1 = z1;
    out->outputThermalVars.z2 = z2;
    out->outputThermalVars.z3 = z3;
    out->outputThermalVars.z4 = z4;
    out->outputThermalVars.z5 = z5;
    out->outputThermalVars.z6 = z6;
    out->outputThermalVars.z7 = z7;
    
    return out;
}


