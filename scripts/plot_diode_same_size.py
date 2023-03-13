from process_utils import *
import os



if __name__ == "__main__":

    # /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI
    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]

    R = []
    I = []
    V = []
    labels = []
    log_V = []
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
        if (len(measurements[0]) != 361):
            print(len(measurements[0]))
            #adj_measurements = resample_single_EE312_data(measurements[2], 21)
            #R.append(adj_measurements)
            print("hereerererererer")
            adj_measurements = resample_single_EE312_data(measurements[0], 21)
            ameasurements = adj_measurements

            adj_measurements = resample_single_EE312_data(measurements[1], 21)
            V.append(adj_measurements)

            #adj_measurements = resample_single_EE312_data(measurements[4], 21)
            #R.append(adj_measurements)


            labels.append(filename)
            counter = counter + 1
            continue

        ameasurements = measurements

        #R.append(measurements[2])
        idx = 0

        V.append(measurements[1])
        temp_log = []
        for v_step in measurements[1]:
            temp_log.append(np.log(abs(v_step)))

        log_V.append(temp_log)
        #R.append(measurements[4])
        labels.append(filename)
        counter = counter + 1

    
   # plot_multiple_EE312_data(ameasurements[0], units[0], name[0], R, units[2], name[2], labels, markers)
   

 

    #plot_multiple_EE312_data(measurements[0], units[0], name[0], R, units[2], name[4], labels, markers)
    plot_multiple_EE312_data(measurements[0], "V", name[0], V, "A", name[1], labels, markers)
    plot_multiple_EE312_data(measurements[0], "V", name[0], log_V, "Log(A)", name[1], labels, markers)


    #Calculate Mean and STD
    V_np = np.array(V)

    #Find mean and std of axis 1
    V_np_means = np.mean(V, axis=0)
    V_np_std = np.std(V, axis=0)

    V_means = list(V_np_means)
    V_std = list(V_np_std)

    #plot_single_EE312_data_with_STD()
    plot_single_EE312_data_with_STD(measurements[0], "V", name[0], V_means, "A", name[1], "Mean Current", 'o', V_std)
