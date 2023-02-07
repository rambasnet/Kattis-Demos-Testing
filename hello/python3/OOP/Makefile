all: check_types test run

test:
	pytest test_hello.py
	pytest test_main.py
	@echo "All unittesting worked!"

run:
	@python main.py | diff - data/1.ans
	@echo "Program worked on sample data!" 

check_types:
	mypy --disallow-untyped-defs --strict main.py
	mypy --disallow-untyped-defs --strict hello.py
	mypy --disallow-untyped-defs --strict test_hello.py
	mypy --disallow-untyped-defs --strict test_main.py