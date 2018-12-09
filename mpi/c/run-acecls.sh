#!/bin/sh
#PBS -N 'qn_test_mpi'
#PBS -q Q1
#PBS -j oe
#PBS -l nodes=4:ppn=4

####################################################
NODES=4
NCORES_NODE=4
NPROCS=`expr $NODES \* $NCORES_NODE`

DIR=.
EXE=$DIR/test_hello
EXE=$DIR/reduce

cd $PBS_O_WORKDIR
pwd
echo "mpirun -machinefile $PBS_NODEFILE --mca btl openib,self -np $NPROCS $EXE"
mpirun -machinefile $PBS_NODEFILE --mca btl openib,self -np $NPROCS $EXE
