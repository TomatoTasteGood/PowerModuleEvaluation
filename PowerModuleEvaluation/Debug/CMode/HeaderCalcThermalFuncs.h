// 2019_12_24, hzc
//
//
#ifndef HEADER_CALC_THERMAL_FUNCS_H_
#define HEADER_CALC_THERMAL_FUNCS_H_


typedef struct{
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
}thermalVars;


typedef struct{
    double powerLossIGBT;
    double powerLossDiode;
    double tSample;
    double tempAmbient;
    thermalVars lastThermalVars;
    int typePowerModule;
    int typePad;
    int typeSolver;
}calcThermalFuncsInput;

typedef struct{
    thermalVars outputThermalVars;
}calcThermalFuncsOutput;

__declspec(dllexport) calcThermalFuncsOutput * funcThermal(calcThermalFuncsInput *p);









#endif

