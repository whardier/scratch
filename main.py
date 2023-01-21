import cython

if not cython.compiled:
    from _metify import print_copyright

print_copyright()

if __name__ == "__main__":
    print('Interesting...')
