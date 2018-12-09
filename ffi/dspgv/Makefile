EXES = test_f test_c
OBJS = test_f.o test_c.o
all: $(EXES)
LIBFILE =

LIBDIR=/usr/lib64

######################################
######################################
######################################
CC = gcc
FC = gfortran
CXX = g++
LD = gcc
LD = gfortran

CCFLAGS = -Wall -fPIC -g -I.
FCFLAGS = -Wall -fPIC -g
LDFLAGS = -Wall -fPIC -g -lgfortran -L$(LIBDIR) -lblas -llapack
LDFLAGS = -Wall -fPIC -g -lblas -llapack
LDSOFLAGS = -Wall -fPIC -g -shared -Wl,-soname,$(LIBFILE) -lgfortran

######################################
######################################
######################################

.SUFFIXES: .f90 .f .c .cpp .o
.f90.o:
	$(FC) $(FCFLAGS) -c $<
.f.o:
	$(FC) $(FCFLAGS) -c $<
.c.o:
	$(CC) $(CCFLAGS) -c $<
.cpp.o:
	$(CXX) $(CCFLAGS) -c $<

exe: test_f test_c

test_f: test_f.o
	$(FC) $(LDFLAGS) -o test_f test_f.o
test_c: test_c.o
	$(LD) $(LDFLAGS) -o test_c test_c.o

######################################
######################################
######################################
clean:
	-rm $(OBJS) $(EXES)
	-rm wrap_dspgv.pyc
	-rm -rf __pycache__
	-rm core-python*
