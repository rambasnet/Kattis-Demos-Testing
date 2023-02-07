all: check_types test run

check_types:
	mypy --disallow-untyped-defs --strict main.py
	mypy --disallow-untyped-defs --strict main_singleton.py
	mypy --disallow-untyped-defs --strict kattis.py
	mypy --disallow-untyped-defs --strict test_solution.py
	mypy --disallow-untyped-defs --strict test_triangle.py
	@echo "Static type check done."

test:
	pytest test_solution.py
	pytest test_triangle.py
	@echo "Unittesting done."

run:
	cat data/1.in | python main.py | diff - data/1.ans
	cat data/1.in | python main_singleton.py | diff - data/1.ans
	@echo "Local kattis sample data test done."
