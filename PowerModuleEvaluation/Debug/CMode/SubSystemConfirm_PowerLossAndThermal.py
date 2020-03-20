# 2019_12_26, hzc
#
#
import ctypes
#
import time
#
import numpy as np
import matplotlib.pyplot as plt
#
dll_Modulation = ctypes.CDLL(r"CalcModulationFuncs.dll")
dll_PowerLoss = ctypes.CDLL(r"CalcPowerLossFuncs.dll")
dll_Thermal = ctypes.CDLL(r"CalcThermalFuncs.dll")
#
class CalcModulationFuncsInput(ctypes.Structure):
    _fields_ = [("t",ctypes.c_double),
                ("indexM",ctypes.c_double),
                ("theta",ctypes.c_double),
                ("freqBase",ctypes.c_double),
                ("typeModulation",ctypes.c_int)
               ]

class CalcModulationFuncsOutput(ctypes.Structure):
    _fields_ = [("uCmdA",ctypes.c_double),
                ("uCmdB",ctypes.c_double),
                ("uCmdC",ctypes.c_double)
               ]

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

class CalcPowerLossFuncsInput(ctypes.Structure):
    _fields_ = [("i",ctypes.c_double),
                ("uCmd",ctypes.c_double),
                ("tempIGBT",ctypes.c_double),
                ("tempDiode",ctypes.c_double),
                ("vDc",ctypes.c_double),
                ("tSw",ctypes.c_double),
                ("rGon", ctypes.c_double),
                ("rGoff", ctypes.c_double),
                ("typePowerModule", ctypes.c_int),
                ("deadTime", ctypes.c_double)
    ]

class CalcPowerLossFuncsOutput(ctypes.Structure):
    _fields_ = [("eOnIGBT1",ctypes.c_double),
                ("eOffIGBT1",ctypes.c_double),
                ("eCondIGBT1",ctypes.c_double),
                ("eSwIGBT1", ctypes.c_double),
                ("eOnIGBT2",ctypes.c_double),
                ("eOffIGBT2",ctypes.c_double),
                ("eCondIGBT2",ctypes.c_double),
                ("eSwIGBT2", ctypes.c_double),
                ("eCondDiode1", ctypes.c_double),
                ("eRecDiode1", ctypes.c_double),
                ("eCondDiode2", ctypes.c_double),
                ("eRecDiode2", ctypes.c_double)
    ]

dll_Modulation.funcUCmdGenerator.argtype = ctypes.POINTER(CalcModulationFuncsInput)
dll_Modulation.funcUCmdGenerator.restype = ctypes.POINTER(CalcModulationFuncsOutput)
dll_Thermal.funcThermal.argtype = ctypes.POINTER(CalcThermalFuncsInput)
dll_Thermal.funcThermal.restype = ctypes.POINTER(CalcThermalFuncsOutput)
dll_PowerLoss.funcPowerLossPerSwitch.argtype = ctypes.POINTER(CalcPowerLossFuncsInput)
dll_PowerLoss.funcPowerLossPerSwitch.restype = ctypes.POINTER(CalcPowerLossFuncsOutput)
#
rGon = 2.4
rGoff = 3.6
vDc = 1073
freqSw = 2000.0
tSw = 1/freqSw
freqBase = 6.0
tBase = 1/freqBase
iBase = 425.0
pf = -0.8845
indexM = 0.256
tempAmbient = 35.0
deadTime = 5e-6
tHeatSink = 45
tTot = tHeatSink*9

typePowerModule = 0
typePad = 0
typeSolver = 0
typeModulation = 0

theta = np.arccos(pf)
numSwCycleTot = int(tTot/tSw)
#
tempIGBT1Avg = tempAmbient
tempDiode1Avg = tempAmbient
tempIGBT2Avg = tempAmbient
tempDiode2Avg = tempAmbient

pCondIGBT1List = []
pCondIGBT2List = []
pSwIGBT1List = []
pSwIGBT2List = []
pCondDiode1List = []
pCondDiode2List = []
pSwDiode1List = []
pSwDiode2List = []
pIGBT1TotList = []
pDiode2TotList = []

y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
y7 = tempAmbient
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
z6 = 0
z7 = tempAmbient

y7List = []
z7List = []

#
# case1 
#



#
# case2
#
print("numSwCycleTot: ",numSwCycleTot)
timeStart = time.time()
for i in range(numSwCycleTot):
    iCurrent = iBase*np.sqrt(2)*np.sin(freqBase*2*np.pi*i*tSw)
    dataCalcModulationFuncsInput = CalcModulationFuncsInput(tSw*i, indexM, theta, freqBase, typeModulation)
    dataCalcModulationFuncsOutput = dll_Modulation.funcUCmdGenerator(ctypes.byref(dataCalcModulationFuncsInput))
    uCurrent = dataCalcModulationFuncsOutput.contents.uCmdA
    dataCalcPowerLossFuncsInput = CalcPowerLossFuncsInput(iCurrent, uCurrent, y7, z7, vDc, tSw, rGon, rGoff, typePowerModule, deadTime)
    dataCalcPowerLossFuncsOutput = dll_PowerLoss.funcPowerLossPerSwitch(ctypes.byref(dataCalcPowerLossFuncsInput))
    pSwIGBT1 = dataCalcPowerLossFuncsOutput.contents.eSwIGBT1*freqSw
    pCondIGBT1 = dataCalcPowerLossFuncsOutput.contents.eCondIGBT1*freqSw
    pSwDiode1 = dataCalcPowerLossFuncsOutput.contents.eRecDiode1*freqSw
    pCondDiode1 = dataCalcPowerLossFuncsOutput.contents.eCondDiode1*freqSw
    pIGBT1Tot = pSwIGBT1+pCondIGBT1
    pDiode1Tot = pSwDiode1+pCondDiode1
    dataCalcThermalFuncsInput = CalcThermalFuncsInput(pIGBT1Tot, pDiode1Tot, tSw, tempAmbient, (y1,y2,y3,y4,y5,y6,y7,z1,z2,z3,z4,z5,z6,z7), typePowerModule, typePad, typeSolver)
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
    y7List.append(y7)
    z7List.append(z7)
    # print("turns:",i)
    # print("pIGBT1Tot:",pIGBT1Tot)
    # print("pDiode1Tot:",pDiode1Tot)
    # print("y1:",y1)
    # print("y2:",y2)
    # print("y3:",y3)
    # print("y4:",y4)
    # print("y5:",y5)
    # print("y6:",y6)
    # print("y7:",y7)
    # print("z1:",z1)
    # print("z2:",z2)
    # print("z3:",z3)
    # print("z4:",z4)
    # print("z5:",z5)
    # print("z6:",z6)
    # print("z7:",z7)
timeEnd = time.time()

print("time: %.3f" % (timeEnd-timeStart))

plt.figure()
plt.plot(y7List,"*-",label="igbt")
plt.plot(z7List,"*-",label="diode")
plt.grid()
plt.legend()
plt.show()







































