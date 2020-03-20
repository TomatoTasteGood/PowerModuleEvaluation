// 2019_12_23, hzc
//
//
#ifndef HEADER_CALC_MODULATION_FUNCS_H_
#define HEADER_CALC_MODULATION_FUNCS_H_

typedef struct{
    double t;
    double indexM;
    double theta;
    double freqBase;
    int typeModulation;
}calcModulationFuncsInput;


typedef struct{
    double uCmdA;
    double uCmdB;
    double uCmdC;
}calcModulationFuncsOutput;

__declspec(dllexport) calcModulationFuncsOutput *funcUCmdGenerator(calcModulationFuncsInput *p);

double arrayMaxData(double *array, int len);
double arrayMinData(double *array, int len);



#endif

