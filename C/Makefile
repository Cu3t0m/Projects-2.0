CC=gcc
CFLAGS=-I.
BIN=bin
PROG_NAME=PROG1

build: main.o
	$(CC) -o $(BIN)/main main.o

run: main.o
	@$(CC) -o $(BIN)/main main.o
	@$(BIN)/main

compress: 
	mkdir -p ${PROG_NAME}
	cp -R main main.c main.o ${PROG_NAME}
	tar -cf ${PROG_NAME}.tar ${PROG_NAME}
	gzip ${PROG_NAME}.tar
	rm -rf ${PROG_NAME}
	@echo "#############"
	@echo "# All done! #"
	@echo "#############"
