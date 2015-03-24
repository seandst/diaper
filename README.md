Sometimes you just need to put a diaper on it.

= wat? =

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

= seriously? =

I guess that's up to you...

= AUTHORS =
Original implementation by Milan Falešník <mfalesni@redhat.com>
Context manager support and module created by Sean Myers <semyers@redhat.com>
