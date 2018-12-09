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

MPIRUN=mpirun
NODEFILE=${PJM_O_NODEINF}
#####################
DIR=.
EXE=${DIR}/test_hello
EXE=${DIR}/reduce

######################
${MPIRUN} -n ${NUM_PROCS} -machinefile ${NODEFILE} --mca plm_rsh_agent /bin/pjrsh -npernode 1 ${EXE}   # openmpi
