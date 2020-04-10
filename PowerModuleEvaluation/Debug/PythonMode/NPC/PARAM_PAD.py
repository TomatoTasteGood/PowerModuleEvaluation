# 2020_03_20, hzc
#
#
import numpy as np
import matplotlib.pyplot as plt
#
param={}
#
param["Test_3L"] = {}
param["Test_3L"]["R_TH_HEATSINK"] = 0.10
param["Test_3L"]["T_TH_HEATSINK"] = 45.0
param["Test_3L"]["C_TH_HEATSINK"] = param["Test_3L"]["T_TH_HEATSINK"] / param["Test_3L"]["R_TH_HEATSINK"]

#
param["Test_Buck_2L"] = {}
param["Test_Buck_2L"]["R_TH_HEATSINK"] = 0.10
param["Test_Buck_2L"]["T_TH_HEATSINK"] = 45.0
param["Test_Buck_2L"]["C_TH_HEATSINK"] = param["Test_Buck_2L"]["T_TH_HEATSINK"] / param["Test_Buck_2L"]["R_TH_HEATSINK"]