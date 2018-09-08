# stackoverflow-52124836
Code to illustrate [this answer on SO](https://stackoverflow.com/a/52239754/2650249).

## Setup

```sh
$ git clone https://github.com/hoefling/stackoverflow-52124836
...
$ cd stackoverflow-52124836/
$ yarn install
...
```
Generate `istanbul` coverage report first:

```sh
$ node_modules/.bin/istanbul cover node_modules/.bin/_mocha

  Array
    #length
      ✓ should be 0 when the array is empty
      ✓ should be 1 when the array has one element
      ✓ should be 2 when the array has two elements

  Array
    #indexOf()
      ✓ should return -1 when the value is not present


  4 passing (5ms)

=============================================================================
Writing coverage object [/private/tmp/stackoverflow-52124836/coverage/coverage.json]
Writing coverage reports at [/private/tmp/stackoverflow-52124836/coverage]
=============================================================================

=============================== Coverage summary ===============================
Statements   : 100% ( 14/14 )
Branches     : 100% ( 0/0 )
Functions    : 100% ( 8/8 )
Lines        : 100% ( 14/14 )
================================================================================
```

Now run python tests with `pytest`. Notice the `istanbul` coverage is included in the `coverage` report:

```sh
$ python -m pytest -sv --cov=py --cov=js --cov-report=term-missing
=================================== test session starts ===================================
platform darwin -- Python 3.6.4, pytest-3.7.3, py-1.5.4, pluggy-0.7.1 --
 /Users/hoefling/.virtualenvs/stackoverflow/bin/python
cachedir: .pytest_cache
rootdir: /private/tmp/stackoverflow-52124836, inifile:
plugins: cov-2.5.1
collected 1 item

py/test_spam.py::test_spam PASSED

---------- coverage: platform darwin, python 3.6.4-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
js/array.length.spec.js      14      0   100%
js/array.spec.js              8      0   100%
py/test_spam.py               2      0   100%
-------------------------------------------------------
TOTAL                        24      0   100%

================================ 1 passed in 0.56 seconds =================================
```
