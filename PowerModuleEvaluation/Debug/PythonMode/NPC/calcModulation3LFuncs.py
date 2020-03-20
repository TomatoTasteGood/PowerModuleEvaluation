# 2020_03_19, hzc
#
#
import numpy as np
import matplotlib.pyplot as plt
#
def funcUCmdGenerator3L(t, index_m, theta, freq_base, type_modulation):
    omega_base = freq_base*np.pi*2
    u_base_A0 = index_m*np.sin(omega_base*t+theta)
    u_base_B0 = index_m*np.sin(omega_base*t+theta-np.pi*2.0/3.0)
    u_base_C0 = index_m*np.sin(omega_base*t+theta+np.pi*2.0/3.0)
    if(type_modulation == "SPWM"):
        u_out_A = u_base_A0
        u_out_B = u_base_B0
        u_out_C = u_base_C0
    elif(type_modulation == "SVPWM"):
        u_delta = -0.5*(max(u_base_A0, u_base_B0, u_base_C0)+min(u_base_A0, u_base_B0, u_base_C0))
        u_out_A = u_base_A0+u_delta
        u_out_B = u_base_B0+u_delta
        u_out_C = u_base_C0+u_delta
    elif(type_modulation == "DPWM1"):
        if(abs(max(u_base_A0, u_base_B0, u_base_C0))> abs(min(u_base_A0, u_base_B0, u_base_C0))):
            u_delta = 1-max(u_base_A0, u_base_B0, u_base_C0)
        else:
            u_delta = -1-min(u_base_A0, u_base_B0, u_base_C0)
        u_out_A = u_base_A0+u_delta
        u_out_B = u_base_B0+u_delta
        u_out_C = u_base_C0+u_delta
    return [u_out_A, u_out_B, u_out_C]

#
if __name__ == "__main__":
    type_modulation = "DPWM1"
    list_t = np.linspace(0,1/5,100)
    list_A = []
    list_B = []
    list_C = []
    for i in list_t:
        a, b, c = funcUCmdGenerator3L(i, 0.9, 0, 5, type_modulation)
        list_A.append(a)
        list_B.append(b)
        list_C.append(c)
    plt.figure()
    plt.plot(list_t, list_A)
    plt.plot(list_t, list_B)
    plt.plot(list_t, list_C)
    plt.grid()
    plt.show()


