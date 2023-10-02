#!/usr/bin/env python3
from mpi4py import MPI # cause the mpi4py library to be initialized
import teca

# ***********************
# set control parameters
# ***********************
# Note that these could be turned in to command line arguments
# if this was a pipeline that was run repeatedly.
# ---------------------------------------------------------------------
# this is the path to the output directory from the previous step
teca_season_max_path = "/glade/scratch/tobrien/clemson_teca_tutorial/02_teca_bard/solution/teca_bard_yearly/"

# create a bounding box that covers western North America
min_lon = -150 + 360 # the +360 is to convert from -180,180 to 0,360
max_lon = -90 + 360 # the +360 is to convert from -180,180 to 0,360
min_lat = 20
max_lat = 60

# set the output variable name
output_variable = 'AR_Rx1day'

# set the output file name
output_file = 'teca_bard.b.e21.BHISTsmbb.f09_g17.LE2-1251.020.cam.h2.Rx1day.WNasubset.%t%.nc'

# ---------------------------------------------------------------------

# ********************************************
# set up the analysis pipeline steps
# reader -> norm-> subset -> rename -> writer
# ********************************************
# ---------------------------------------------------------------------
# create a stage to read the data
reader = teca.teca_cf_reader.New()
reader.set_files_regex(f'{teca_season_max_path}/.*\.nc')
reader.set_z_axis_variable('') # indicate that there is no vertical axis

# create a stage to normalize the coordinates so we can be 
# certain about the latitude ordering
norm = teca.teca_normalize_coordinates.New()
norm.set_input_connection(reader.get_output_port()) # connect to the reader

# create a stage to compute the spatial subset
subset = teca.teca_cartesian_mesh_subset.New()
subset.set_input_connection(norm.get_output_port()) # connect to the normalization step
subset.set_bounds([min_lon, max_lon, min_lat, max_lat, 0, 0,]) # set the spatial subset (we use 0,0 for the vertical bounds because there is no vertical axis)

# create a stage that renames the variables
rename = teca.teca_rename_variables.New()
rename.set_input_connection(subset.get_output_port()) # connect to the subset step
rename.set_original_variable_names(['ar_wgtd_PRECT']) # set the original variable name
rename.set_new_variable_names([output_variable]) # set the new variable name

# create a stage to write the data
writer = teca.teca_cf_writer.New()
writer.set_input_connection(rename.get_output_port()) # connect to the rename step
writer.set_file_name(output_file) # set the output file name
writer.set_point_arrays([output_variable]) # set the output variable name
writer.set_thread_pool_size(1) # only use one thread for this step since python is single threaded
writer.set_layout('yearly') # set the file layout to yearly

# ---------------------------------------------------------------------

# *****************
# run the pipeline
# *****************
# ---------------------------------------------------------------------
# the last algorithm in the pipeline is responsible for triggering the
# execution of the pipeline. In this case the writer will execute the
# pipeline when it is 'updated'.
writer.update()
# ---------------------------------------------------------------------