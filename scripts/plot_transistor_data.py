import matplotlib.pyplot as plt
import numpy as np
from process_utils import *
import os





if __name__ == "__main__":

    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]

    R = []
    I = []
    V = []
    labels = []
    ameasurements = []
    units = []
    name = []
    markers = ['bs', 'g^', 'ro', 'y+', 'o', 'b+', 'r^', 'bo', 'g+' ]

    counter = 0
    for filename in os.listdir(dirname):

     
        if (counter == 5):
            break

        print(filename)
        path_and_file = dirname + "/" + filename
        measurements, units, name = read_EE312_CSV(path_and_file)

        # All should have same dimension
        print("###########################")
        print(len(measurements[0]))
        print("###########################")
        if (len(measurements[0]) != 402):
            print(len(measurements[0]))
            #adj_measurements = resample_single_EE312_data(measurements[2], 21)
            #R.append(adj_measurements)
            print("hereerererererer")
            adj_measurements = resample_single_EE312_data(measurements[0], 21)
            ameasurements = adj_measurements

            adj_measurements = resample_single_EE312_data(measurements[2], 21)
            V.append(adj_measurements)

            #adj_measurements = resample_single_EE312_data(measurements[4], 21)
            #R.append(adj_measurements)


            labels.append(filename)
            counter = counter + 1
            continue

        ameasurements = measurements

        #R.append(measurements[2])
        idx = 0

        V.append(measurements[2])
        #R.append(measurements[4])
        labels.append(filename)
        counter = counter + 1


    plot_multiple_EE312_data(measurements[0], units[0], name[0], V, units[2], name[2], labels, markers)