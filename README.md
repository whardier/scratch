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
creating build/temp.linux-x86_64-3.9/lib
x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -Ilib/ -I/home/spencersr/tmp/cython-test/.venv/include -I/usr/include/python3.9 -c lib/metify.c -o build/temp.linux-x86_64-3.9/lib/metify.o
x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -Ilib/ -I/home/spencersr/tmp/cython-test/.venv/include -I/usr/include/python3.9 -c main.c -o build/temp.linux-x86_64-3.9/main.o
creating build/lib.linux-x86_64-3.9
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -Wl,-z,relro -g -fwrapv -O2 -g -ffile-prefix-map=/build/python3.9-RNBry6/python3.9-3.9.2=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.9/lib/metify.o build/temp.linux-x86_64-3.9/main.o -o build/lib.linux-x86_64-3.9/main.cpython-39-x86_64-linux-gnu.so
copying build/lib.linux-x86_64-3.9/main.cpython-39-x86_64-linux-gnu.so ->

(.venv) spencersr@dev:~/tmp/cython-test/scratch$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
Copyright (c) 2021-2023 Metify Inc.
All rights reserved.
https://www.metify.io
>>>

(.venv) spencersr@dev:~/tmp/cython-test/scratch$ ls -las
total 468
  4 drwxr-xr-x 5 spencersr spencersr   4096 Jan 21 00:59 .
  4 drwxr-xr-x 5 spencersr spencersr   4096 Jan 21 00:57 ..
  4 drwxr-xr-x 4 spencersr spencersr   4096 Jan 21 00:58 build
  4 -rw-r--r-- 1 spencersr spencersr     58 Jan 21 00:54 build.sh
  4 drwxr-xr-x 8 spencersr spencersr   4096 Jan 21 00:59 .git
  4 drwxr-xr-x 2 spencersr spencersr   4096 Jan 21 00:58 lib
228 -rw-r--r-- 1 spencersr spencersr 233207 Jan 21 00:58 main.c
200 -rwxr-xr-x 1 spencersr spencersr 202840 Jan 21 00:58 main.cpython-39-x86_64-linux-gnu.so
  4 -rw-r--r-- 1 spencersr spencersr     67 Jan 21 00:55 main.pxd
  4 -rw-r--r-- 1 spencersr spencersr    270 Jan 21 00:57 main.py
  4 -rw-r--r-- 1 spencersr spencersr   2501 Jan 21 00:59 README.md
  4 -rw-r--r-- 1 spencersr spencersr    225 Jan 21 00:50 setup.py

(.venv) spencersr@dev:~/tmp/cython-test/scratch$ strings main.cpython-39-x86_64-linux-gnu.so | grep "Metif"
Copyright (c) 2021-2023 Metify Inc.
```
