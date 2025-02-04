EXEC = play/executable
FILE = $(EXEC)
OBJECT = ./romanCipher.o

CFLAGS = -g

$(EXEC): $(OBJECT)
	gcc $(OBJECT) $(CFLAGS) -o $(FILE)
	rm $(OBJECT)
	./$(EXEC)


clean:
	rm $(OBJECT) $(FILE) 

run:
	./$(FILE)

rungdb:
	gdb ./$(FILE)

runvalgrind:
	valgrind ./$(FILE)