# distutils: sources = lib/metify.c
# distutils: include_dirs = lib/

import cython

if not cython.compiled:
    def print_copyright():
        pass

print_copyright()

# Do regular code things below this line ...

if __name__ == "__main__":
    print('Interesting...')
