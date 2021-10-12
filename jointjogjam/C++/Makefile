COMPILER = g++
COMPILER_FLAGS = -Wall -std=c++17
PROGRAM_NAME = jointjogjam.exe
CPP_FILES = *.cpp

build:
	$(COMPILER) $(COMPILER_FLAGS) $(CPP_FILES) -o $(PROGRAM_NAME)

local_test:
	./$(PROGRAM_NAME) test

kattis_test:
	cat ../1.in | ./$(PROGRAM_NAME) | diff - ../1.ans
	cat ../2.in | ./$(PROGRAM_NAME) | diff - ../2.ans
	cat ../3.in | ./$(PROGRAM_NAME) | diff - ../3.ans
	echo "all Kattis sample tests cases passed..."

clean:
	rm -f $(PROGRAM_NAME) *.o