
# Usage

To plot data, do the following:
1. make a New python file. You can copy and pasted "plot_contact_chain.py" as a staring point
2. Make sure the line "from process_utils import *" is at the top.
3. Use functions from process_utils.py to plot your data


## plot_single_EE312_data

This function takes the following arguments:
1. x axis data array  (for example voltage sweep). Should by a Python array
2. x axis unit (for example volts). Should be a string
3. x axis name (for example V1). Should be a string 
4. y axis data array  (for example voltage sweep). Should by a Python array
5. y axis unit (for example ohms). Should be a string
6. y axis label (for example the filename) Should be a string
7.  x axis name (for example V1). Should be a string 
8. Marker (for example 'bs' for blue square). Vals can be found here:



Example: plot_single_EE312_data(measurements[0], units[0], name[0], measurements[2], units[2], label, name[2], 'bs')


<img width="752" alt="image" src="https://user-images.githubusercontent.com/54165966/222874959-d8461e64-ab85-4680-8158-c960308afa34.png">




<img width="904" alt="image" src="https://user-images.githubusercontent.com/54165966/222874519-6f9a6162-50fe-4107-9a63-923da34adc18.png">
