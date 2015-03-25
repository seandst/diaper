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

```

seriously?
==========

I guess that's up to you...

DOCS
====

http://diaper.rtfd.org/

AUTHORS
=======
Original implementation by Milan Falešník <mfalesni@redhat.com>
Context manager support and module created by Sean Myers <semyers@redhat.com>

BADGES
======

[![Build Status](https://travis-ci.org/seandst/diaper.svg?branch=master)](https://travis-ci.org/seandst/diaper)
[![Coverage Status](https://coveralls.io/repos/seandst/diaper/badge.svg?branch=master)](https://coveralls.io/r/seandst/diaper?branch=master)
[![Documentation Status](https://readthedocs.org/projects/diaper/badge/?version=latest)](https://readthedocs.org/projects/diaper/?badge=latest)
