import matplotlib.pyplot as plt
import numpy as np
from process_utils import *

# Current uA, delta v, mV (we convert to A, V)
die_a5_si = [[86.03600E-6, 25.14E-3, 10], [120.540E-6, 67.97E-3, 20], [144.560E-6 , 81.52E-3, 30]]
#SBZ , well mayboe not should but we DID measure 0 and that made semi sense given our weird scope/manip setup
#Current NA, delta V
die_a5_gate = [[-4.780E-12, 0, 10], [68.880E-12, 0, 20], [ -3.020E-12, 0, 30], [-4.230E-12, 0, 40], [-3.610E-12, 0, 50]]


# Current uA, delta v, mV (we convert to A, V)
die_d6_si = [[91.0360E-6, 57.99E-3, 10], [125.320E-6, 69.38E-3, 20], [150.960E-6 , 82.52E-3, 30]]
die_d6_gate = [[5.47E-12, 0, 10], [53.19E-12, 0, 20],  [1.15E-12, 0, 30]]


die_f2_si = [[91.0360E-6, 56.27E-3, 10], [125.320E-6, 70.27E-3, 20], [150.960E-6 , 84.27E-3, 30]]
die_f2_gate = [[5.47E-12, 0, 10], [53.19E-12, 0, 20],  [1.15E-12, 0, 30]]

die_g3_si = [[91.0360E-6, 53.48E-3, 10], [125.320E-6, 70.11E-3, 20], [150.960E-6 , 81.47E-3, 30]]
die_g3_gate = [[5.47E-12, 0, 10], [53.19E-12, 0, 20],  [1.15E-12, 0, 30]]



def get_plotting_params(arr):


    x = []
    y = []
    s = []

    idx = 0
    for i in range(len(arr)):

        if (idx >= 3):
            break

        i_34 = arr[idx][0]
        s_param = arr[idx][2]
        x.append(i_34)
        s.append(s_param)

        sheet_resistance = (arr[idx][1] * s_param )/(80*i_34)
        y.append(sheet_resistance)
        idx = idx + 1

    return x, y, s


if __name__ == "__main__":


    x_a5_si,r_a5_si,s_a5 = get_plotting_params(die_a5_si)
    x_d6_si,r_d6_si,s_a5 = get_plotting_params(die_d6_si)
    x_f2_si,r_f2_si,s_a5 = get_plotting_params(die_f2_si)
    x_g3_si,r_g3_si,s_a5 = get_plotting_params(die_g3_si)

    r_si_mean = []
    r_si_std = []
    for r1,r2,r3,r4 in zip(r_a5_si,r_d6_si,r_f2_si,r_g3_si):

        sum_arr = [r1,r2,r3,r4]
        mean = np.mean(sum_arr)
        std = np.std(sum_arr)
        r_si_mean.append(mean)
        r_si_std.append(std)




    fig, ax = plt.subplots()
    ax.scatter(s_a5, r_a5_si, c='b', marker="s", label='A5')
    ax.scatter(s_a5, r_d6_si, c='r', marker="o", label='D6')
    ax.scatter(s_a5, r_f2_si, c='g', marker="+", label='F2')
    ax.scatter(s_a5, r_g3_si, c='y', marker="^", label='G3')
    plt.legend(loc='upper left')

    # for i, txt in enumerate(s_a5):
    #     ax.annotate(txt, (x_a5_si[i], r_a5_si[i]))
    #     ax.annotate(txt, (x_d6_si[i], r_d6_si[i]))

    plt.xlabel("Width (um)")
    plt.ylabel("Sheet Resistivity (ohm/sq)")
    plt.title("Si Van der Pauw Sheet Resistivity vs Width Parameter for Dice A5, D6, F2, and G3")
    plt.show()


    fig, ax = plt.subplots()
    #ax.scatter(s_a5, r_si_mean,  c='y', marker="^", label='Mean')
    ax.errorbar(s_a5, r_si_mean, r_si_std,  c='b', marker="o", label='Mean', linestyle='none')
    plt.legend(loc='upper left')
    plt.xlabel("Width (um)")
    plt.ylabel("Sheet Resistivity (ohm/sq)")
    plt.title("Mean Van der Pauw Si Sheet Resistivity vs Width Parameter Across Dice A5, D6, F2, and G3")
    plt.show()



    x_a5_gate,r_a5_gate,s_a5 = get_plotting_params(die_a5_gate)
    x_d6_gate,r_d6_gate,s_a5 = get_plotting_params(die_d6_gate)
    x_f2_gate,r_f2_gate,s_a5 = get_plotting_params(die_f2_gate)
    x_g3_gate,r_g3_gate,s_a5 = get_plotting_params(die_g3_gate)


    fig, ax = plt.subplots()
    ax.scatter(s_a5, r_a5_gate, c='b', marker="s", label='A5')
    ax.scatter(s_a5, r_d6_gate, c='r', marker="o", label='D6')
    ax.scatter(s_a5, r_f2_gate, c='g', marker="+", label='F2')
    ax.scatter(s_a5, r_g3_gate, c='y', marker="^", label='G3')

    # for i, txt in enumerate(s_a5):
    #     ax.annotate(txt, (x_a5_si[i], r_a5_si[i]))
    #     ax.annotate(txt, (x_d6_si[i], r_d6_si[i]))

    plt.xlabel("Width (um)")
    plt.ylabel("Sheet Resistivity (ohm/sq)")
    plt.title("Gate Sheet Resistivity vs Width Parameter for Dice A5, D6, F2, and G3")
    plt.show()

    

    #plot_single_EE312_data(x, "Current (A)", "I34", y, "ohm/sq", "Sheet Resistivity", "die_a5", 'b+')


