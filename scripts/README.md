
# Usage

To plot data, do the following:
1. make a New python file. You can copy and pasted "plot_contact_chain.py" as a staring point
2. Make sure the line "from process_utils import *" is at the top.
3. Use functions from process_utils.py to plot your data
4. Consult the API below for details


# API


## plot_single_EE312_data

This function takes the following arguments:
1. x axis data array  (for example voltage sweep). Should by a Python array
2. x axis unit (for example volts). Should be a string
3. x axis name (for example V1). Should be a string 
4. y axis data array  (for example voltage sweep). Should by a Python array
5. y axis unit (for example ohms). Should be a string
6. y axis name (for example V1). Should be a string 
7. y axis label (for example the filename) Should be a string
8. Marker (for example 'bs' for blue square). Vals can be found here: https://matplotlib.org/stable/api/markers_api.html

NOTE: At the moment this plot does not save the plot automatically. Screenshot it or save from GUI that pops up

Example: plot_single_EE312_data(measurements[0], units[0], name[0], measurements[2], units[2], label, name[2], 'bs')


<img width="752" alt="image" src="https://user-images.githubusercontent.com/54165966/222874959-d8461e64-ab85-4680-8158-c960308afa34.png">



## plot_multiple_EE312_data

This function takes the following arguments:
1. x axis data array  (for example voltage sweep). Should by a Python array
2. x axis unit (for example volts). Should be a string
3. x axis name (for example V1). Should be a string 
4. y axis data array(S)  (for example voltage sweep). Should by a Python ARRAY of arrays
5. y axis unit (for example ohms). Should be a string
6. y axis name (for example V1). Should be a string 
7. y axis label(S) (for example the filename) Should be a Python ARRAY 
8. Marker (for example 'bs' for blue square). THIS IS AN ARRAY HERE.  Vals can be found here: https://matplotlib.org/stable/api/markers_api.html

NOTE: At the moment this plot does not save the plot automatically. Screenshot it or save from GUI that pops up

Example:  plot_multiple_EE312_data(measurements[0], units[0], name[0], R, units[2], name[2], labels, markers)

<img width="752" alt="image" src="https://user-images.githubusercontent.com/54165966/222875204-305d3355-ff49-4e87-8509-02d56c1ea4fd.png">


## read_EE312_CSV

This function takes the following arguments:
1. filename. Should by a FULL PATH file name. Example: /Users/chris/Desktop/EE312_Final_Project/EE312-Final-Project/EE_312_2023_Friday/contact_chain_B6_SI/Contact_Chain_B6_C=0.5.csv

This function returns the following:
1. measurements = [] This is a multidimensional array, where each measurement corresponds to a different measurement dimension. This function will print which dimension is which, along with their units. For example measurements[0], could contain ALL the voltage sweep voltages [0,0.01,0.02,..], and measurements[2] could contain all the resitance measurements [1000,1004,998,..]
2. units = []. This array holds the units corresponding to each dimension of measurements. For example units[0] = "V" (a string), and units[2] = "ohms"
3. name = []. This array holds the name corresponding to each dimension of measurements. For example name[0] = "V1" (a string), and name[2] = "R"



## compute_mean
1. This function takes in an array and returns  the mean (average)

## compute_std
1. This function takes in an array and returns  the standard deviation (variance squared)




