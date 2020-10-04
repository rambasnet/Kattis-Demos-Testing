COMPILER = g++
COMPILER_FLAGS = -Wall -std=c++17
PROGRAM_NAME = oddities.exe
CPP_FILES = oddities.cpp

build:
	$(COMPILER) $(COMPILER_FLAGS) $(CPP_FILES) -o $(PROGRAM_NAME)

unit_tests:
	./$(PROGRAM_NAME) test

kattis_tests:
	cat ../1.in | ./$(PROGRAM_NAME) | diff - ../1.ans
	echo "all Kattis sample tests cases passed..."

clean:
	rm -f $(PROGRAM_NAME) *.o