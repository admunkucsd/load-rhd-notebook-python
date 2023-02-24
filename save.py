from importrhdutilities import *
filename = 'input.rhd' # Change this variable to load a different data file
result, data_present = load_file(filename)
result["amplifier_data"].transpose().tofile("output.dat") # Change this to whatever you would like the output file name to be