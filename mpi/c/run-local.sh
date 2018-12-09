#!/bin/sh

NPROCS=8
DIR=.
EXE=${DIR}/test_hello
EXE=${DIR}/reduce

mpirun -n $NPROCS $EXE
