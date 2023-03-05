from process_utils import *
import os
import numpy as np



if __name__ == "__main__":

    # /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI
    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]

    R = []
    labels = []
    ameasurements = []
    units = []
    name = []
    markers = ['bs', 'g^', 'ro', 'y+', 'o', 'b+', 'r^', 'bo', 'g+' ]



    counter = 0
    for filename in os.listdir(dirname):

     
        if (counter == 9):
            break

        print(filename)
        path_and_file = dirname + "/" + filename
        measurements, units, name = read_EE312_CSV(path_and_file)

        if (len(measurements[0]) != 21):
            adj_measurements = resample_single_EE312_data(measurements[2], 21)
            R.append(adj_measurements)
            labels.append(filename)
            counter = counter + 1
            continue

        ameasurements = measurements

        R.append(measurements[2])
        labels.append(filename)
        counter = counter + 1

    
    #plot_multiple_EE312_data(ameasurements[0], units[0], name[0], R, units[2], name[2], labels, markers)



    R_np = np.array(R)
    print(R_np.shape)

    #Find mean and std of axis 1
    R_np_means = np.mean(R, axis=0)
    R_np_std = np.std(R, axis=0)

    R_means = list(R_np_means)
    R_std = list(R_np_std)

    print(R_means)
    print(R_std)
    

    plot_single_EE312_data_with_STD(ameasurements[0], units[0], name[0], R_np_means, units[2], name[2], labels[0], markers[0], R_std)

