from process_utils import *
import os
import numpy as np



if __name__ == "__main__":

    # /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI
    if (len(sys.argv) != 2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] , "/path/to/files/ \n")
      
    dirname = sys.argv[1]


    units = []
    name = []
    markers = ['bs', 'g^', 'ro', 'y+', 'o', 'b+', 'r^', 'bo', 'g+', 'b<', 'bv', 'b^', 'bD', 'g<', 'gv', 'g^', 'gD', 'r<', 'rv', 'c+', 'c<',  'y^', 'yD', 'y<', 'yv', 'm+', 'mo', 'm<', 'm^' ]

    #markers = ['bs', 'b+', 'b*', 'bx', 'bp', 'b^', 'bo', 'gs', 'g+', 'g*', 'gx', 'gp', 'g^', 'go', 'rs', 'r+', 'r*', 'rx', 'rp', 'r^', 'ro', 'ys', 'y+', 'y*', 'yx', 'yp', 'y^', 'yo', 'ms', 'm+', 'm*', 'mx', 'mp', 'm^', 'mo']


    counter = 0
    for dir in os.listdir(dirname):


        if (".DS_Store" in dir):
            continue

        intermediate_path = dirname + "/" + dir


        full_mat_R = []
        full_mat_I= []
        full_mat_labels = []
        full_mat_measurements = []

        for material_dir in  os.listdir(intermediate_path):

            R = []
            I= []
            labels = []
            measurements = []


            if (".DS_Store" in material_dir):
                continue
           

            material_path = intermediate_path + "/" + material_dir

            for filename in  os.listdir(material_path):

                if (".DS_Store" in filename):
                    continue

      
                print("###########New Observation Below#############")
                print(filename)
                
                path_and_file = material_path + "/" + filename
                measurements, units, name = read_EE312_CSV(path_and_file)

                if (len(measurements[0]) != 21):
                    adj_measurements = resample_single_EE312_data(measurements[2], 21)
                    R.append(adj_measurements)
                    adj_measurements = resample_single_EE312_data(measurements[1], 21)
                    I.append(adj_measurements)
                    labels.append(filename)
                    continue

                measurements = measurements
                full_mat_measurements = measurements

                R.append(measurements[2])
                I.append(measurements[1])
                labels.append(filename)

                full_mat_R.append(measurements[2])
                full_mat_I.append(measurements[1])
                full_mat_labels.append(filename)
            
            #Plot all data for a given material
            plot_multiple_EE312_data(measurements[0], units[0], name[0], R, units[2], name[2], labels, markers)
            plot_multiple_EE312_data(measurements[0], units[0], name[0], I, units[1], name[1], labels, markers)
        
        
        plot_multiple_EE312_data(full_mat_measurements[0], units[0], name[0], full_mat_R, units[2], name[2], full_mat_labels, ['bs', 'b+', 'b*', 'bx', 'bp', 'b^', 'bo', 'gs', 'g+', 'g*', 'gx', 'gp', 'g^', 'go', 'rs', 'r+', 'r*', 'rx', 'rp', 'r^', 'ro', 'ys', 'y+', 'y*', 'yx', 'yp', 'y^', 'yo', 'ms', 'm+', 'm*', 'mx', 'mp', 'm^', 'mo'])
        plot_multiple_EE312_data(full_mat_measurements[0], units[0], name[0], full_mat_I, units[1], name[1], full_mat_labels, ['bs', 'b+', 'b*', 'bx', 'bp', 'b^', 'bo', 'gs', 'g+', 'g*', 'gx', 'gp', 'g^', 'go', 'rs', 'r+', 'r*', 'rx', 'rp', 'r^', 'ro', 'ys', 'y+', 'y*', 'yx', 'yp', 'y^', 'yo', 'ms', 'm+', 'm*', 'mx', 'mp', 'm^', 'mo'])

                
     #/analysis/SerpentineInterdigitated/Smallest_Cont_All/  for continuity (serpentine)
     #/analysis/SerpentineInterdigitated/Smallest_Iso_All/  for isolation (interdigitated)




