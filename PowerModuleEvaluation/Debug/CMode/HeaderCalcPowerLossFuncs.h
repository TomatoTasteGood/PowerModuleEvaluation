// 2019_12_26, hzc
//
//
#ifndef HEADER_CALC_POWERLOSS_FUNCS_H_
#define HEADER_CALC_POWERLOSS_FUNCS_H_

typedef struct{
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
}calcPowerLossFuncsInput;

typedef struct{
    double eOnIGBT1;
    double eOffIGBT1;
    double eCondIGBT1;
    double eSwIGBT1;
    double eOnIGBT2;
    double eOffIGBT2;
    double eCondIGBT2;
    double eSwIGBT2;
    double eCondDiode1;
    double eRecDiode1;
    double eCondDiode2;
    double eRecDiode2;
}calcPowerLossFuncsOutput;

__declspec(dllexport) calcPowerLossFuncsOutput *funcPowerLossPerSwitch(calcPowerLossFuncsInput *p);












#endif
