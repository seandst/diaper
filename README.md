Sometimes you just need to put a diaper on it.

wat?
====

The diaper pattern, in its natural form:
```python
def error_hider():
    try:
        do_something(arg1, arg2=True)
    except:
        pass

```

New and "improved" (*cough*)

```python
import diaper

diaper(do_something, arg1, arg2=True)

# or, if you want, you can wrap a whole block of crap
with diaper:
    do_something(arg1, arg2=True)

# what diaper invocation would be complete without a little silliness
with diaper as nappy:
    assert diaper is nappy, "...in some parts of the world"
```

seriously?
==========

I guess that's up to you...

DOCS
====

http://diaper.rtfd.org/

AUTHORS
=======

- Original implementation by [Milan Falešník](https://github.com/mfalesni)
- Context manager support and module created by [Sean Myers](https://github.com/seandst)
- Diaper 'smell' concept courtesy of [Michael Hrivnak](https://github.com/mhrivnak)

BADGES
======

[![Build Status](https://travis-ci.org/seandst/diaper.svg?branch=master)](https://travis-ci.org/seandst/diaper)
[![Coverage Status](https://coveralls.io/repos/seandst/diaper/badge.svg?branch=master)](https://coveralls.io/r/seandst/diaper?branch=master)
[![Documentation Status](https://readthedocs.org/projects/diaper/badge/?version=latest)](https://readthedocs.org/projects/diaper/?badge=latest)
