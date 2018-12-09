#!/bin/bash
#PJM -N "cx_lecture"
#PJM -L "rscgrp=cx-lecture"
#PJM -L "vnode=8"
#PJM -L "vnode-core=1"
#PJM -P "vn-policy=abs-unpack"
#PJM -L "elapse=00:00:30"
#PJM -j
#PJM -X
#PJM --no-stging

#####################
NUM_NODES=${PJM_VNODES}
NUM_CORES=1
NUM_PROCS=`expr ${NUM_NODES} \* ${NUM_CORES}`

OPENBLAS_NUM_THREADS=1
OPENBLAS_USE_THREADS=0
export OPENBLAS_NUM_THREADS OPENBLAS_USE_THREADS

#PYTHON=/home/python/bin/python3
PYTHON=/home/python/bin/python
MPIRUN=/home/openmpi-1.10.3/bin/mpirun
NODEFILE=${PJM_O_NODEINF}
#####################
DIR=${HOME}/riit_160824/mpi/python
EXE=${DIR}/reduce.py
EXE=${DIR}/test_hello.py

######################
SHELL=/bin/tcsh
export SHELL
${MPIRUN} -n ${NUM_PROCS} -machinefile ${NODEFILE} --mca plm_rsh_agent /bin/pjrsh -npernode 1 ${PYTHON} ${EXE}
