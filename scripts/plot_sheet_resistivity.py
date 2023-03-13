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
        if (len(measurements[0]) != 96):
            #adj_measurements = resample_single_EE312_data(measurements[2], 21)
            #R.append(adj_measurements)
            print("hereerererererer")
            adj_measurements = resample_single_EE312_data(measurements[0], 21)
            ameasurements = adj_measurements

            adj_measurements = resample_single_EE312_data(measurements[3], 21)
            V.append(adj_measurements)

            adj_measurements = resample_single_EE312_data(measurements[4], 21)
            R.append(adj_measurements)


            labels.append(filename)
            counter = counter + 1
            continue

        ameasurements = measurements

        #R.append(measurements[2])
        idx = 0
        for m in measurements[3]:
            measurements[3][idx] = (measurements[3][idx] * 4.53)/(measurements[0][idx]) # TODO Make this a function of W/L
            idx = idx + 1

        V.append(measurements[3])
        R.append(measurements[4])
        labels.append(filename)
        counter = counter + 1

    
   # plot_multiple_EE312_data(ameasurements[0], units[0], name[0], R, units[2], name[2], labels, markers)
    print("##################")
    print(len(measurements[0]))
    print(units[0])
    print(name[0])
    print(len(R))
    print(units[0])
    print(name[0])
 

    plot_multiple_EE312_data(measurements[0], units[0], name[0], R, units[2], name[4], labels, markers)
    plot_multiple_EE312_data(measurements[0], units[0], name[0], V, units[1], name[3], labels, markers)

    #plot_single_EE312_data(measurements[0], units[0], name[0], I[0] * , units[2], name[4], labels[0], markers[0])

    #plot_multiple_EE312_data(x, x_unit, x_name, y_arr, y_unit, y_name, y_label_arr, marker_arr)
