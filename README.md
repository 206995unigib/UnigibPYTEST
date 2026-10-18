# Pytest Class Exercise

This small Python project is for practising how to write and run tests with
`pytest`. It includes simple arithmetic functions and a file-size formatter,
along with tests that check their expected results.

## Setup

Use Python 3. Install pytest if it is not already available:

```powershell
python -m pip install pytest
```

## Run the tests

From the project root, run the complete test suite:

```powershell
python -m pytest -v
```

To run one test file:

```powershell
python -m pytest -v tests/test_adder.py
```

Pytest discovers test files named `test_*.py` and test functions named
`test_*`. Each test uses `assert` to compare the actual result with the
expected result. For example:

```python
from unipackage.adder import add


def test_add_two_numbers():
    assert add(2, 3) == 5
```

For multiple inputs that should produce related results, use
`pytest.mark.parametrize`, as demonstrated in
`tests/test_formatter_disk_size_multiple.py`.

## Challenge: write and test your own function

Add a `multiply(a, b)` function to `unipackage/adder.py`. It should return the
product of its two numbers. Then create `tests/test_multiply.py` and write tests
that check at least:

- `multiply(3, 4)` returns `12`
- `multiply(-2, 3)` returns `-6`
- `multiply(0, 5)` returns `0`

Run just your new test while you work:

```powershell
python -m pytest -v tests/test_multiply.py
```

At first, the test may fail because the function is not implemented yet. Keep
working until pytest reports `1 passed` for each test case (or all tests in the
file pass). Then run the complete suite to check that your change has not
broken the existing exercises:

```powershell
python -m pytest -v
```

## Challenge 2: validate function input

Write a `divide_numbers(numerator, denominator)` function in
`unipackage/adder.py` (or put it in a new module if you prefer). It should
divide the first number by the second, with these rules:

- Accept integers and floating-point numbers.
- Reject strings, even strings that look like numbers such as `"12"`, by
  raising `TypeError`.
- Reject other non-numeric values, such as `None`, by raising `TypeError`.
- Raise `ZeroDivisionError` when the denominator is zero.

Create `tests/test_divide_numbers.py`. Test a normal division, a result with a
remainder (for example, `5 / 2`), a string input, another invalid input, and a
zero denominator. Use `pytest.raises` to check that invalid inputs raise the
expected exception. For example:

```python
import pytest


def test_divide_numbers_rejects_string_input():
    with pytest.raises(TypeError):
        divide_numbers("12", 3)
```

Run the new test file while you work, then run the full suite:

```powershell
python -m pytest -v tests/test_divide_numbers.py
python -m pytest -v
```

## Project contents

- `unipackage/adder.py` contains the `add` and `subtract` functions.
- `formatter/disk_size.py` contains `format_file_size`, which formats
  non-negative byte counts using binary units (B, KB, MB, GB, TB, and above).
- `tests/` contains the pytest functions for those modules.
- `main.py` is a command-line example for formatting one file size. For
  example: `python main.py 2048`.

When adding a function, add or update tests under `tests/`, then run pytest
again to check the behavior.
