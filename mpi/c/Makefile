CC = mpicc
CCFLAGS = -g #-O3
LDFLAGS = -g #-O3

OBJS_HELLO = test_hello.o
OBJS_REDUCE = reduce.o
EXE_HELLO = test_hello
EXE_REDUCE = reduce

all: ${EXE_HELLO} ${EXE_REDUCE}

${EXE_HELLO}: ${OBJS_HELLO}
	${CC} ${LDFLAGS} -o ${EXE_HELLO} ${OBJS_HELLO}
${EXE_REDUCE}: ${OBJS_REDUCE}
	${CC} ${LDFLAGS} -o ${EXE_REDUCE} ${OBJS_REDUCE}

test_hello.o: test_hello.c
	${CC} ${CCFLAGS} -c test_hello.c
reduce.o: reduce.c
	${CC} ${CCFLAGS} -c reduce.c

clean:
	-rm ${OBJS_HELLO} ${OBJS_REDUCE}
	-rm ${EXE_HELLO}  ${EXE_REDUCE}

clean_files:
	-rm qn_*
