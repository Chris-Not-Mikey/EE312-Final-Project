from process_utils import *
import os



if __name__ == "__main__":

    # /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI
    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]

    R = []
    I = []
    labels = []
    ameasurements = []
    units = []
    name = []
    markers = ['bs', 'g^', 'ro', 'y+', 'o', 'b+', 'r^', 'bo', 'g+', 'm+' ]

    counter = 0
    for filename in os.listdir(dirname):

        if (filename == ".DS_Store"):
            continue
     
        if (counter == 9):
            break

        print(filename)
        path_and_file = dirname + "/" + filename
        measurements, units, name = read_EE312_CSV(path_and_file)

        # All should have same dimension
        print("###########################")
        print(len(measurements[0]))
        print("###########################")
        if (len(measurements[0]) != 21):
            adj_measurements = resample_single_EE312_data(measurements[2], 21)
            R.append(adj_measurements)
            adj_measurements = resample_single_EE312_data(measurements[1], 21)
            #ameasurements =  resample_single_EE312_data(measurements[0], 21)
            I.append(adj_measurements)
            labels.append(filename)
            counter = counter + 1
            continue

        ameasurements = measurements

        R.append(measurements[2])
        I.append(measurements[1])
        labels.append(filename)
        counter = counter + 1

    print(name)
    print(len(R))
    #plot_multiple_EE312_data(ameasurements[0], units[0], name[0], R, units[2], name[2], labels, markers)


    plot_multiple_EE312_data(ameasurements[0], units[0], name[0], I, units[1], name[1], labels, markers)


