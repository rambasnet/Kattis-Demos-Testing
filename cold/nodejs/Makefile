PROGRAM_NAME = cold.js

install:
	npm install
	npm audit fix

local_test:
	npm run test

kattis_test:
	cat ../1.in | node $(PROGRAM_NAME) | diff - ../1.ans
	cat ../2.in | node $(PROGRAM_NAME) | diff - ../2.ans
	echo "all Kattis sample tests cases passed..."

clean:
	echo "all clean up done!"
	