COMPILER = g++
COMPILER_FLAGS = -Wall -std=c++17
PROGRAM_NAME = helpaphd.exe
CPP_FILES = helpaphd.cpp

build:
	$(COMPILER) $(COMPILER_FLAGS) $(CPP_FILES) -o $(PROGRAM_NAME)

unit_test:
	./$(PROGRAM_NAME) test

kattis_test:
	cat ../1.in | ./$(PROGRAM_NAME) | diff - ../1.ans
	echo "all Kattis sample tests cases passed..."

clean:
	rm -f $(PROGRAM_NAME) *.o