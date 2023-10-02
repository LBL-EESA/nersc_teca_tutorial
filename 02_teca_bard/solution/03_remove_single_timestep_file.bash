#!/bin/sh

# TECA BARD produces one file (for 2015) that has a single timestep;
# that causes problems for the daily average operator, which is a bug we need to fix.  For now, this script removes that file.
rm teca_bard_output/teca_bard.b.e21.BHISTsmbb.f09_g17.LE2-1251.020.cam.h2.2015-01-01-00Z.nc