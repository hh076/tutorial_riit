#!/bin/sh

#PYTHON=/home/python/bin/python3
#PYTHON=/home/python/bin/python
#MPIRUN=/home/openmpi-1.10.3/bin/mpirun
PYTHON=python
MPIRUN=mpirun

NPROCS=8
DIR=.
EXE=${DIR}/reduce.py
EXE=${DIR}/test_hello.py

OPENBLAS_NUM_THREADS=1
OPENBLAS_USE_THREADS=0
export OPENBLAS_NUM_THREADS OPENBLAS_USE_THREADS

#${MPIRUN} -n ${NPROCS} --mca btl_openib_warn_default_gid_prefix 0 ${PYTHON} ${EXE}
${MPIRUN} -n ${NPROCS} ${PYTHON} ${EXE}
