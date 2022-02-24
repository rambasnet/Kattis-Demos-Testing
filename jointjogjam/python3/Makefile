PROGRAM_NAME = jointjogjam.py
TEST_SCRIPT	= simple_test.py

local_test:
	python3 $(TEST_SCRIPT)

kattis_test:
	cat ../1.in | python3 $(PROGRAM_NAME) | diff - ../1.ans
	cat ../2.in | python3 $(PROGRAM_NAME) | diff - ../2.ans
	cat ../3.in | python3 $(PROGRAM_NAME) | diff - ../3.ans
	echo "all Kattis sample tests cases passed..."

clean:
	rm -rf __pycache__
	rm -f *.pyc
	