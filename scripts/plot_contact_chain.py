from process_utils import *
import os



if __name__ == "__main__":

    # /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI
    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]

    R = []
    labels = []
    measurements = []
    units = []
    name = []
    markers = ['bs', 'g^', 'ro', 'y+', 'o' ]

    counter = 0
    for filename in os.listdir(dirname):

     
        if (counter == 5):
            break

        print(filename)
        path_and_file = dirname + "/" + filename
        measurements, units, name = read_EE312_CSV(path_and_file)

        # All should have same dimension
        if (len(measurements[0]) > 52):
            continue

        R.append(measurements[2])
        labels.append(filename)
        counter = counter + 1

    
    plot_multiple_EE312_data(measurements[0], units[0], name[0], R, units[2], name[2], labels, markers)

