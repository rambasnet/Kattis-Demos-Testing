all: check_types test run

test:
	pytest test_solution.py
	pytest test_temperature.py
	@echo "All unittest cases worked..."

run:
	@cat data/1.in | python main.py | diff - data/1.ans
	@cat data/2.in | python main.py | diff - data/2.ans
	@echo "All kattis sample test data test done..."

check_types:
	mypy --disallow-untyped-defs --strict main.py
	mypy --disallow-untyped-defs --strict temperature.py
	mypy --disallow-untyped-defs --strict test_solution.py
	mypy --disallow-untyped-defs --strict test_temperature.py
