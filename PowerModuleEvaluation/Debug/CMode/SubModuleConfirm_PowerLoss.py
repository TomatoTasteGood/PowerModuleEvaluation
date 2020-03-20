# 2019_12_26, hzc
#
#
import ctypes
#
import numpy as np
import matplotlib.pyplot as plt
#
dll_PowerLoss = ctypes.CDLL(r"CalcPowerLossFuncs.dll")
class CalcPowerLossFuncsInput(ctypes.Structure):
    _fields_ = [("i",ctypes.c_double),
                ("uCmd",ctypes.c_double),
                ("tempIGBT",ctypes.c_double),
                ("tempDiode",ctypes.c_double),
                ("vDc",ctypes.c_double),
                ("tSw",ctypes.c_double),
                ("rGon",ctypes.c_double),
                ("rGoff",ctypes.c_double),
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

dll_PowerLoss.funcPowerLossPerSwitch.argtype = ctypes.POINTER(CalcPowerLossFuncsInput)
dll_PowerLoss.funcPowerLossPerSwitch.restype = ctypes.POINTER(CalcPowerLossFuncsOutput)
#
i = 400
uCmd = 0.5
tempIGBT = 125
tempDiode = 125
vDc = 900
tSw = 1/2000.0
typePowerModule = 0
deadTime = 5e-6
rGon =2.4
rGoff = 3.6

dataCalcPowerLossFuncsInput = CalcPowerLossFuncsInput(i, uCmd, tempIGBT, tempDiode, vDc, tSw, rGon, rGoff, typePowerModule, deadTime)
dataCalcPowerLossFuncsOutput = dll_PowerLoss.funcPowerLossPerSwitch(ctypes.byref(dataCalcPowerLossFuncsInput))

eOnIGBT1 = dataCalcPowerLossFuncsOutput.contents.eOnIGBT1
eOffIGBT1 = dataCalcPowerLossFuncsOutput.contents.eOffIGBT1
eSwIGBT1 = dataCalcPowerLossFuncsOutput.contents.eSwIGBT1
eCondIGBT1 = dataCalcPowerLossFuncsOutput.contents.eCondIGBT1
eRecDiode2 = dataCalcPowerLossFuncsOutput.contents.eRecDiode2
eCondDiode2 = dataCalcPowerLossFuncsOutput.contents.eCondDiode2
#
print("eOnIGBT1", eOnIGBT1)
print("eOffIGBT1", eOffIGBT1)
print("eSwIGBT1", eSwIGBT1)
print("eCondIGBT1", eCondIGBT1)
print("eRecDiode2", eRecDiode2)
print("eCondDiode2", eCondDiode2)


