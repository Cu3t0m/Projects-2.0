CC=gcc
CFLAGS=-I.

PROG_NAME=PROG1

build: main.o
	$(CC) -o main main.o

test: main.o
	@$(CC) -o main main.o
	@./main

compress: 
	mkdir -p ${PROG_NAME}
	cp -R main main.c main.o ${PROG_NAME}
	tar -cf ${PROG_NAME}.tar ${PROG_NAME}
	gzip ${PROG_NAME}.tar
	rm -rf ${PROG_NAME}
	@echo "#############"
	@echo "# All done! #"
	@echo "#############"