PROGRAM_NAME = egypt.js

install:
	npm install
	npm audit fix

local_test:
	npm run test

kattis_test:
	cat ../1.in | node $(PROGRAM_NAME) | diff - ../1.ans
	echo "all Kattis sample tests cases passed..."

clean:
	echo "all clean up done!"
	