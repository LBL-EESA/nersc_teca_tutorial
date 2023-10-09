#!/bin/bash
#SBATCH -J test_heatwave
#SBATCH --nodes 4
#SBATCH --constraint cpu
#SBATCH --account m1517
#SBATCH --time 00:15:00
#SBATCH -q debug

# load the CPU-only version of teca
module use /global/common/software/m1517/teca/perlmutter_cpu/develop/modulefiles/
module load teca

time srun -n 512 python3   \
                        -u \
                        -m mpi4py \
                        06_test_teca_heatwave_detect

