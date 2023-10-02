#!/bin/sh

# create a directory that contains links to all the HighResMIP files that we want to analyze for a particular run

LINK_DIR=`pwd -P`/linked_files
mkdir -p ${LINK_DIR}

# set the HighResMIP_BASE directory
RUN_BASE="/global/cfs/cdirs/m3522/cmip6/CMIP6_hrmcol/HighResMIP/CMIP6/HighResMIP/ECMWF/ECMWF-IFS-HR/highresSST-present/r1i1p1f1"

# enter the link directory
pushd $LINK_DIR
# link humidity
ln -s  ${RUN_BASE}/6hrPlevPt/hus/gr/v20170915/hus_*.nc .
# link zonal wind
ln -s  ${RUN_BASE}/6hrPlevPt/ua/gr/v20170915/ua_*.nc .
# link meridional wind
ln -s  ${RUN_BASE}/6hrPlevPt/va/gr/v20170915/va_*.nc .
# link precipitation
ln -s ${RUN_BASE}/Prim6hr/pr/gr/v20170915/pr_*.nc .
# exit the link directory
popd

# write the link directory name to the terminal for checking in the MCF file
echo 'Make sure that the `data_root` directory in the MCF file matches the directory below:'
echo $LINK_DIR
