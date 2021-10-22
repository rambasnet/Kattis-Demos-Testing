#!/ usr/bin/env python3

"""
separate test file for pytest
pytest recursively discovers all the files with test* and runs the
assert statements in them
"""

from hello import answer

def test_answer():
    assert answer() == "Hello World!"
    print('all test cases passed...')

if __name__ == "__main__":
  test_answer()