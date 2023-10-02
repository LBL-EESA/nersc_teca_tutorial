#!/bin/bash
#SBATCH -C cpu
#SBATCH -N 1
#SBATCH -q debug
#SBATCH -J teca_metadata_probe
#SBATCH -t 00:15:00
#SBATCH -A m1517
#SBATCH -oe
#SBATCH -o teca_cf_restripe.%j.out

# load the CPU-only version of teca, suitable for the CPU partition
module use /global/common/software/m1517/teca/perlmutter_cpu/develop/modulefiles/
module load teca

# run the teca_metadata_probe executable
srun -n 128 teca_metadata_probe \
    --input_file ECMWF-IFS-HR_highresSST-present_r1i1p1f1.mcf