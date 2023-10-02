#!/bin/bash
#SBATCH -J check_e5_dataset
#SBATCH --nodes 4
#SBATCH --constraint cpu
#SBATCH --account m1517
#SBATCH --time 00:15:00
#SBATCH -q debug

# load the CPU-only version of teca
module use /global/common/software/m1517/teca/perlmutter_cpu/develop/modulefiles/
module load teca

time srun -n 512 teca_metadata_probe --input_file era5_combined_dataset.mcf
