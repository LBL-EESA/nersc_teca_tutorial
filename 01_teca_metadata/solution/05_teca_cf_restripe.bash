#!/bin/bash
#SBATCH -C cpu
#SBATCH -N 78
#SBATCH -q regular
#SBATCH -J teca_cf_restripe
#SBATCH -t 00:75:00
#SBATCH -A m1517
#SBATCH -oe
#SBATCH -o teca_cf_restripe.%j.out

# load teca
module use /global/common/software/m1517/teca/perlmutter_cpu/develop/modulefiles/
module load teca

# set the output variables
export POINT_ARRAYS="T Z Q W VAR_2T SP TCW CAPE VIWVE VIWVN"

# set the MCF file
export MCF_FILE=/global/cfs/cdirs/m1517/cascade/taobrien/nersc_teca_tutorial/01_teca_metadata/solution/era5_combined_dataset.mcf

# create the output directory
export OUT_DIR=${SCRATCH}/nersc_teca_tutorial/era5_combined_north_america/
mkdir -p ${OUT_DIR}

# set the bounds of the restriped data
# format: lon0 lon1 lat0 lat1 z0 z1
BOUNDS="215 325 15 65 50 1000"

# use restripe to extract data for the north american continent and a bit into the pacific and atlantic oceans
time srun -n 128 \
    teca_cf_restripe \
        --input_file=${MCF_FILE} \
        --output_file=${OUT_DIR}/era5_combined_north_america_%t%.nc \
        --file_layout=daily \
        --bounds ${BOUNDS} \
        --point_arrays ${POINT_ARRAYS} \
        --normalize_coordinates




