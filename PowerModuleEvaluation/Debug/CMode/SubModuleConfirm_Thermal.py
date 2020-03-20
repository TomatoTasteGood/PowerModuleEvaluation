# 2019_12_26, hzc 
#
#
import ctypes
#
import numpy as np
import matplotlib.pyplot as plt
#
dll_Thermal = ctypes.CDLL(r"CalcThermalFuncs.dll")
class thermalVars(ctypes.Structure):
    _fields_ = [("y1",ctypes.c_double),
                ("y2",ctypes.c_double),
                ("y3",ctypes.c_double),
                ("y4",ctypes.c_double),
                ("y5",ctypes.c_double),
                ("y6",ctypes.c_double),
                ("y7",ctypes.c_double),
                ("z1",ctypes.c_double),
                ("z2",ctypes.c_double),
                ("z3",ctypes.c_double),
                ("z4",ctypes.c_double),
                ("z5",ctypes.c_double),
                ("z6",ctypes.c_double),
                ("z7",ctypes.c_double),
    ]

class CalcThermalFuncsInput(ctypes.Structure):
    _fields_ = [("powerLossIGBT", ctypes.c_double),
                ("powerLossDiode", ctypes.c_double),
                ("tSample", ctypes.c_double),
                ("tempAmbient", ctypes.c_double),
                ("lastThermalVars", thermalVars),
                ("typePowerModule", ctypes.c_int),
                ("typePad", ctypes.c_int),
                ("typeSolver", ctypes.c_int)
    ]

class CalcThermalFuncsOutput(ctypes.Structure):
    _fields_ = [("outputThermalVars", thermalVars)
    ]

dll_Thermal.funcThermal.argtype = ctypes.POINTER(CalcThermalFuncsInput)
dll_Thermal.funcThermal.restype = ctypes.POINTER(CalcThermalFuncsOutput)
#
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
y7 = 0
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
z6 = 0
z7 = 0
y1List = []
y2List = []
y3List = []
y4List = []
y5List = []
y6List = []
y7List = []
z1List = []
z2List = []
z3List = []
z4List = []
z5List = []
z6List = []
z7List = []
tSample = 1/2000.0
tCalc = 5
numCalc = int(tCalc/tSample)
tempAmbient = 45
powerLossIGBTPeak = 1000
powerLossDiodePeak = 1000
typeSolver = 0
typePowerModule = 0
typePad = 0
#
for i in range(numCalc):
    powerLossIGBT = powerLossIGBTPeak*np.sin(i*tSample*5)
    if(powerLossIGBT<=0):
        powerLossIGBT = 0
    powerLossDiode = powerLossDiodePeak*np.sin(i*tSample*5+np.pi)
    if(powerLossDiode<=0):
        powerLossDiode = 0
    y1List.append(y1)
    y2List.append(y2)
    y3List.append(y3)
    y4List.append(y4)
    y5List.append(y5)
    y6List.append(y6)
    y7List.append(y7)
    z1List.append(z1)
    z2List.append(z2)
    z3List.append(z3)
    z4List.append(z4)
    z5List.append(z5)
    z6List.append(z6)
    z7List.append(z7)
    dataCalcThermalFuncsInput = CalcThermalFuncsInput(powerLossIGBT, powerLossDiode, tSample, tempAmbient, (y1,y2,y3,y4,y5,y6,y7,z1,z2,z3,z4,z5,z6,z7), typePowerModule, typePad, typeSolver)
    dataCalcThermalFuncsOutput = dll_Thermal.funcThermal(ctypes.byref(dataCalcThermalFuncsInput))
    y1 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y1
    y2 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y2
    y3 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y3
    y4 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y4
    y5 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y5
    y6 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y6
    y7 = dataCalcThermalFuncsOutput.contents.outputThermalVars.y7
    z1 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z1
    z2 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z2
    z3 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z3
    z4 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z4
    z5 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z5
    z6 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z6
    z7 = dataCalcThermalFuncsOutput.contents.outputThermalVars.z7

plt.figure()
plt.plot(y7List,"*-",label="y7")
plt.plot(z7List,"*-",label="z7")
plt.grid()
plt.legend()
plt.show()


































































































