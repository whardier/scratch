# scratch


```shell
(.venv) spencersr@dev:~/tmp/cython-test/scratch$ bash ./build.sh
Compiling main.py because it changed.
[1/1] Cythonizing main.py
/home/spencersr/tmp/cython-test/.venv/lib/python3.9/site-packages/Cython/Compiler/Main.py:345: FutureWarning: Cython directive 'language_level' not set, using '3str' for now (Py3). This has changed from earlier releases! File: /home/spencersr/tmp/cython-test/scratch/main.pxd
  tree = Parsing.p_module(s, pxd, full_module_name)
running build_ext
building 'main' extension
creating build
creating build/temp.linux-x86_64-3.9
x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/home/spencersr/tmp/cython-test/.venv/include -I/usr/include/python3.9 -c main.c -o build/temp.linux-x86_64-3.9/main.o
creating build/lib.linux-x86_64-3.9
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -Wl,-z,relro -g -fwrapv -O2 -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.9/main.o -o build/lib.linux-x86_64-3.9/main.cpython-39-x86_64-linux-gnu.so
copying build/lib.linux-x86_64-3.9/main.cpython-39-x86_64-linux-gnu.so ->

(.venv) spencersr@dev:~/tmp/cython-test/scratch$ python3 -m entrypoint
Using _metify.pxd
Copyright (c) 2021-2023 Metify Inc.
All rights reserved.
https://www.metify.io
{'thing': 1, 'compiled': True}

(.venv) spencersr@dev:~/tmp/cython-test/scratch$ rm main.cpython-39-x86_64-linux-gnu.so
(.venv) spencersr@dev:~/tmp/cython-test/scratch$ python3 -m entrypoint
Using _metify.py
Copyright (c) 2021-2023 Metify Inc.
All rights reserved.
https://www.metify.io
{'thing': 1, 'compiled': False}

```
