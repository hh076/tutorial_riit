OBJS    = sort_c.o sort_f.o sort_f95.o sort_cpp.o
LIBFILE = libsort.so

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
LDFLAGS = -Wall -fPIC -g -shared -Wl,-soname,$(LIBFILE) -lgfortran -lstdc++
LDFLAGS = -Wall -fPIC -g -shared -lstdc++

######################################
######################################
######################################
all: $(LIBFILE)

$(LIBFILE): $(OBJS)
	$(LD) $(LDFLAGS) $(OBJS) -o $(LIBFILE)

.SUFFIXES: .f95 .f .c .cpp .o
.f95.o:
	$(FC) $(FCFLAGS) -c $<
.f.o:
	$(FC) $(FCFLAGS) -c $<
.c.o:
	$(CC) $(CCFLAGS) -c $<
.cpp.o:
	$(CXX) $(CCFLAGS) -c $<

clean: clean_exe
	-rm $(OBJS)
	-rm $(LIBFILE)
	-rm mysort.mod wrap_sort.pyc
	-rm -rf __pycache__

######################################
######################################
######################################
exe: test_c test_f test_f95 test_cpp
test_c: test_c.c $(LIBFILE)
	$(CC) $(CCFLAGS) -o test_c test_c.c -L. -lsort
test_f: test_f.f $(LIBFILE)
	$(FC) $(FCFLAGS) -o test_f test_f.f -L. -lsort
test_f95: test_f95.f95 $(LIBFILE)
	$(FC) $(FCFLAGS) -o test_f95 test_f95.f95 -L. -lsort
test_cpp: test_cpp.cpp $(LIBFILE)
	$(CXX) $(FCFLAGS) -o test_cpp test_cpp.cpp -L. -lsort

clean_exe:
	-rm test_c
	-rm test_f
	-rm test_f95
	-rm test_cpp
