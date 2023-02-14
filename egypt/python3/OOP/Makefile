all: check_types unittest localtest

check_types:
	mypy --disallow-untyped-defs --strict main.py
	mypy --disallow-untyped-defs --strict main_singleton.py
	mypy --disallow-untyped-defs --strict kattis.py
	mypy --disallow-untyped-defs --strict test_solution.py
	mypy --disallow-untyped-defs --strict test_triangle.py
	@echo "Static type check done."

unittest:
	pytest test_solution.py
	pytest test_triangle.py
	@echo "Unittest done."

localtest:
	cat data/1.in | python main.py | diff - data/1.ans
	cat data/1.in | python main_singleton.py | diff - data/1.ans
	@echo "Local kattis sample data test done."
