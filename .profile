#Root dirs
DIR_PYTHON=$HOME/Python
DIR_MPI=$HOME/local/openmpi-1.10.3
DIR_LIBLAPACK=$HOME/local/lib

#For python, python3, mpicc, user-defined and mpirun command
PATH=${DIR_PYTHON}/bin:${DIR_MPI}/bin:$PATH

#For libblas.so liblapack, mpi libraries
LD_LIBRARY_PATH=.:${DIR_LIBLAPACK}:${DIR_MPI}/lib:${LD_LIBRARY_PATH}

#I don't know whether these are necessary.
BLAS=${DIR_LIBLAPACK}/libblas.so
LAPACK=${DIR_LIBLAPACK}/liblapack.so

#For python user-defined modules
PYTHONPATH=.:${PYTHONPATH}

#For python numpy. Configurations of threads
OPENBLAS_NUM_THREADS=1
OPENBLAS_USE_THREADS=0

export PATH LD_LIBRARY_PATH BLAS LAPACK PYTHONPATH OPENBLAS_NUM_THREADS OPENBLAS_USE_THREADS
