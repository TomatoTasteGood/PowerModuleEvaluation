// 2019_12_23, hzc
//
//
#include "HeaderConstParam.h"
#include "HeaderCalcModulationFuncs.h"
//
#include "stdlib.h"
#include "math.h"
//

double arrayMaxData(double *array, int len)
{
    int index = 0;
    double max = array[index];
    for(index=1; index<len; index++)
    {
        if(max<array[index])
        {
            max = array[index];
        }
    }
    return max;
}

double arrayMinData(double *array, int len)
{
    int index = 0;
    double min = array[index];
    for(index=1; index<len; index++)
    {
        if(min>array[index])
        {
            min = array[index];
        }
    }
    return min;
}


calcModulationFuncsOutput *funcUCmdGenerator(calcModulationFuncsInput *p)
{
    double t;
    double indexM;
    double theta;
    double freqBase;
    int typeModulation;
    double omegaBase;
    double uBaseAbc[3];
    double uDelta;
    double uCmdAbc[3];

    calcModulationFuncsOutput *out = (calcModulationFuncsOutput *)calloc(1,sizeof(calcModulationFuncsOutput));
    //
    // input 
    t = p->t;
    indexM = p->indexM;
    theta = p->theta;
    freqBase = p->freqBase;
    typeModulation = p->typeModulation;
    omegaBase = freqBase*2*PI;

    uBaseAbc[0] = indexM*sin(omegaBase*t+theta);
    uBaseAbc[1] = indexM*sin(omegaBase*t+theta-PI/3.0*2.0);
    uBaseAbc[2] = indexM*sin(omegaBase*t+theta+PI/3.0*2.0);

    switch(typeModulation)
    {
        case 0:
             uCmdAbc[0] = uBaseAbc[0];
             uCmdAbc[1] = uBaseAbc[1];
             uCmdAbc[2] = uBaseAbc[2];
             break;
        case 1:
            uDelta = -0.5*(arrayMaxData(uBaseAbc, 3)+arrayMinData(uBaseAbc, 3));
            uCmdAbc[0]= uBaseAbc[0]+uDelta;
            uCmdAbc[1]= uBaseAbc[1]+uDelta;
            uCmdAbc[2]= uBaseAbc[2]+uDelta;
            break;
        case 2:
            if(fabs(arrayMaxData(uBaseAbc, 3))>=fabs(arrayMinData(uBaseAbc, 3)))
            {
                uDelta = 1-arrayMaxData(uBaseAbc, 3);
            }
            else
            {
                uDelta = -1-arrayMinData(uBaseAbc, 3);
            }
            uCmdAbc[0]= uBaseAbc[0]+uDelta;
            uCmdAbc[1]= uBaseAbc[1]+uDelta;
            uCmdAbc[2]= uBaseAbc[2]+uDelta;
            break;
        default:
            uCmdAbc[0] = 0;
            uCmdAbc[1] = 0;
            uCmdAbc[2] = 0;
            break;
    }
    // 
    //out
    out->uCmdA = uCmdAbc[0];
    out->uCmdB = uCmdAbc[1];
    out->uCmdC = uCmdAbc[2];

    return out;


}
