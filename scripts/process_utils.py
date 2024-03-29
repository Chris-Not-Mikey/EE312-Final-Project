# For EE 312 @ Stanford
# Author: Chris Calloway, cmc2374@stanford.edu
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

 

#/Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI/Contact_Chain_B6_C=0.5.csv




def read_EE312_CSV(f):

    measurements = []
    units = []
    name = []

    # Number of observations of Micromanipulator software made (eg ' V1', ' I1', ' R', ' Rsheet')
    num_measures = 0
    repeat_status = 0 # Seems like the CSV repeats itself at some point(?)

    with open(f, mode ='r')as file:
   
        csvFile = csv.reader(file)
 
        # displaying the contents of the CSV file
        
        data_lines_read = 0

        for line in csvFile:
                
                # Skip the lines that don't give us data, or the Names of what we are measuring

                # Get units
                if (len(line) > 1 and repeat_status == 0):
                    if ("Analysis.Setup.Vector.List.Datum.Unit" in line[1]):
                        num_measures = len(line[2:])

                        for meas in range(num_measures):
                            units.append(line[meas+2])

                        units.append("arb")
                        units.append("arb")
                        units.append("arb")
                        units.append("arb")
                        
                        print("Units")
                        print(units)
                         



                
                #print(line)
                if (str(line[0]) == "DataName"):

                    if (repeat_status == 1):
                        # End parsing, we have already seen this data (TODO: Investigate this)
                        break 
                    
                    repeat_status = repeat_status + 1

                    # Find number of measurements (columns after DataName)
                    num_measures = len(line[1:])
                    index = 0

                    # Store an array for each measurement in  variable measurements = []
                    for meas in range(num_measures):
                        #print("Index ", index, "holds", line[meas+1], "(", units[index], ")")
                        print(meas)
                        name.append(str(line[meas+1]))
                        # Give empty array per measurement
                        measurements.append([])
                        index = index + 1
                         
                        
                
                if (str(line[0]) == "DataValue"):
                    
                    # Get each data and store in global array
                    for meas in range(num_measures):
                    
                        #Get dimension of measurements[], and to that dimension add new data
                        #print(line)
                        #Sometimes the CSV file adds blank entries. Sigh...
                        if (line[meas+1] == ' '):
                            #print("here")
                            continue
                        measurements[meas].append(float(line[meas+1]))
                
                    
                    data_lines_read = data_lines_read + 1

        return measurements, units, name


def compute_mean(arr):

    if (len(arr) < 1):
        print("ERROR: Need to read CSV data first!")
        return -1

    return np.average(arr)


def compute_std(arr):

    if (len(arr) < 1):
        print("ERROR: Need to read CSV data first!")
        return -1

    return np.std(arr)


def compute_multi_dimensional_mean(arr):
  
    R_np = np.array(arr)
    print(R_np.shape)
    #Find mean and std of axis 1
    R_np_means = np.mean(R, axis=0)

    R_means = list(R_np_means)


    return R_means


def compute_multi_dimensional_std(arr):

  
    R_np = np.array(arr)
    print(R_np.shape)
    #Find mean and std of axis 1
    R_np_std = np.std(R, axis=0)

    R_means = list(R_np_std)


    return R_means


# Resample data to smaller size (ie account for different step size in measurement)
def resample_single_EE312_data(arr, size):

    resampled_arr = []
    #print(arr)

    old_size = len(arr)
    step = int(old_size/size)

    idx = 0
   
    for i in range(size):
        #print(idx)
        resampled_arr.append(arr[idx])
        idx = idx + step
     
    return resampled_arr


# Plot a single MEAN Y vs X, with error bar for standard deviation Specify the type of marker as well (eg bs == blue square) 
def plot_single_EE312_data_with_STD(x, x_unit, x_name, y, y_unit, y_name, y_label, marker, std):

    plt.errorbar(x, y, std, label=y_label, uplims=True, lolims=True, linestyle='none', fmt='s')
    plt_title_str = y_name + " vs" + x_name
    x_axis_str =  x_name + "(" + x_unit + ")"
    y_axis_str =  y_name + "(" + y_unit + ")"
    plt.suptitle(plt_title_str)
    plt.xlabel(x_axis_str)
    plt.ylabel(y_axis_str)
    #plt.legend(loc="lower right")
    plt.show()


# Plot a single Y vs X. Specify the type of marker as well (eg bs == blue square)
def plot_single_EE312_data(x, x_unit, x_name, y, y_unit, y_name, y_label, marker):

    plt.plot(x, y, marker, label=y_label)
    plt_title_str = y_name + " vs" + x_name
    x_axis_str =  x_name + "(" + x_unit + ")"
    y_axis_str =  y_name + "(" + y_unit + ")"
    plt.suptitle(plt_title_str)
    plt.xlabel(x_axis_str)
    plt.ylabel(y_axis_str)
    plt.legend(loc="lower right")
    plt.show()

# Plot multiple Y vs one X. Specify the type of marker(s) as well (eg bs == blue square)
def plot_multiple_EE312_data(x, x_unit, x_name, y_arr, y_unit, y_name, y_label_arr, marker_arr):

    plt.plot(x, y_arr[0], marker_arr[0], label=y_label_arr[0])

    plt_title_str = y_name + " vs" + x_name
    x_axis_str =  x_name + "(" + x_unit + ")"
    y_axis_str =  y_name + "(" + y_unit + ")"

   

    index = 0
    for i in y_arr:

        # Sloppy, but avoids double writing
        if (index == 0):
            index = index + 1
            continue

        plt.plot(x, y_arr[index], marker_arr[index], label=y_label_arr[index])
        plt.suptitle(plt_title_str)
        plt.xlabel(x_axis_str)
        plt.ylabel(y_axis_str)
      
        index = index + 1

    # Now with everthing, display plot
    plt.legend(y_label_arr)
    plt.show()


# Plot multiple Y vs one X. Specify the type of marker(s) as well (eg bs == blue square)
def plot_multiple_EE312_data_log(x, x_unit, x_name, y_arr, y_unit, y_name, y_label_arr, marker_arr):

    plt.plot(x, y_arr[0], marker_arr[0], label=y_label_arr[0])

    plt_title_str = y_name + " vs" + x_name
    x_axis_str =  x_name + "(" + x_unit + ")"
    y_axis_str =  y_name + "(" + y_unit + ")"

   

    index = 0
    for i in y_arr:

        # Sloppy, but avoids double writing
        if (index == 0):
            index = index + 1
            continue

        plt.plot(x, y_arr[index], marker_arr[index], label=y_label_arr[index], lw=2)
        plt.yscale('log')
        plt.suptitle(plt_title_str)
        plt.xlabel(x_axis_str)
        plt.ylabel(y_axis_str)
      
        index = index + 1

    # Now with everthing, display plot
   
    plt.legend(y_label_arr)
    plt.show()



# Plot multiple Y vs one X. Specify the type of marker(s) as well (eg bs == blue square)
def plot_multiple_EE312_data_save(x, x_unit, x_name, y_arr, y_unit, y_name, y_label_arr, marker_arr):

    plt.plot(x, y_arr[0], marker_arr[0], label=y_label_arr[0])

    plt_title_str = y_name + " vs" + x_name
    x_axis_str =  x_name + "(" + x_unit + ")"
    y_axis_str =  y_name + "(" + y_unit + ")"

   

    index = 0
    for i in y_arr:

        # Sloppy, but avoids double writing
        if (index == 0):
            index = index + 1
            continue

        plt.plot(x, y_arr[index], marker_arr[index], label=y_label_arr[index])
        plt.suptitle(plt_title_str)
        plt.xlabel(x_axis_str)
        plt.ylabel(y_axis_str)
      
        index = index + 1

    # Now with everthing, display plot
    plt.legend(y_label_arr)
    #plt.show()
    return plt
 




    


if __name__ == "__main__":

    if (len(sys.argv) !=2):
        print("Invalid Number of arguments. Usage: python3",sys.argv[0] ,"/path/to/file/filename.csv \n")
      
    filname = sys.argv[1]
    print("Reading ", filname, "and plotting data \n")
    

    measurements, units, name = read_EE312_CSV(filname)


    # Example:
    # Marker options: 'bs', 'g^', 'r--', etc
    tokenized_filename = filname.split("/")
    label = tokenized_filename[-1]
    plot_single_EE312_data(measurements[0], units[0], name[0], measurements[2], units[2], name[2], label, 'bs')

    # Eaxmple
    markers = ['bs', 'g^']
    plot_multiple_EE312_data(measurements[0], units[0], name[0], measurements[1:3], units[1], name[1], name[1:3], markers)




