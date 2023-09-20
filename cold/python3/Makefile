MAIN = cold.py
PY = python3

# target and its dependencies followed by commands
all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All done!"

localtest:
	@cat ../1.in | $(PY) $(MAIN) | diff - ../1.ans
	@cat ../2.in | $(PY) $(MAIN) | diff - ../2.ans
	@echo "All local tests passed!"

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest test_unit_cold.py

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_unit_cold.py

check_types:
	mypy --disallow-untyped-defs --strict cold.py
	mypy --disallow-untyped-defs --strict test_unit_cold.py

check_style:
	flake8 cold.py --count --show-source --statistics

# submit to kattis
submit:
	kattis --problem cold --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc
