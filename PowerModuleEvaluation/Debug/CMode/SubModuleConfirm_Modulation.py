# 2019_12_23, hzc
#
#
import ctypes
#
import numpy as np
import matplotlib.pyplot as  plt
#
dll_Modulation = ctypes.CDLL(r"CalcModulationFuncs.dll")
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

dll_Modulation.funcUCmdGenerator.argtype = ctypes.POINTER(CalcModulationFuncsInput)
dll_Modulation.funcUCmdGenerator.restype = ctypes.POINTER(CalcModulationFuncsOutput)
#
tSw = 1/2000
tCalc = 0.2
numCalc = int(tCalc/tSw)
indexM = 0.9
theta = 0
freqBase = 15.0
typeModulation = 2

listUCmdA = []
listUCmdB = []
listUCmdC = []

for i in range(numCalc):
    dataCalcModulationFuncsInput = CalcModulationFuncsInput(tSw*i, indexM, theta, freqBase, typeModulation)
    dataCalcModulationFuncsOutput = dll_Modulation.funcUCmdGenerator(ctypes.byref(dataCalcModulationFuncsInput))
    uCmdA = dataCalcModulationFuncsOutput.contents.uCmdA
    uCmdB = dataCalcModulationFuncsOutput.contents.uCmdB
    uCmdC = dataCalcModulationFuncsOutput.contents.uCmdC
    listUCmdA.append(uCmdA)
    listUCmdB.append(uCmdB)
    listUCmdC.append(uCmdC)
#
plt.figure()
plt.plot(listUCmdA,"*-",label="uCmdA")
plt.plot(listUCmdB,"*-",label="uCmdB")
plt.plot(listUCmdC,"*-",label="uCmdC")
plt.grid()
plt.legend()
plt.show()