import cython

if not cython.compiled:
    from _metify import print_copyright, get_thing

print_copyright()

