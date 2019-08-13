# Complete instructions for running Boost.Python example on MacOS

It seems quite easy when reading the intruductions on [Boost.Python Example](https://www.boost.org/doc/libs/1_70_0/libs/python/doc/html/tutorial/index.html), right? Writing the codes is easy indeed, but actually running it? No! The repo shows you how to actually run the example.

After trials and errors, here are my steps that is working under Python 3.7, MacOS Mojave 10.14 and Boost 1.70.

Prerequisites: you have installed the necessary building tools and python3. Then:

1. install boost-python3 using homebrew: `brew install boost-python3`;
2. create a clean directory;
3. create a cpp file with the example codes;
4. create setup.py with content like in this repo;
5. create a setup.cfg with content like in this repo;
6. open a terminal, change to this directory, and run: `python3 setup.py build_ext --inplace`;
7. A shared library will be generated in this directory;
8. In the same terminal, run python3;
9. run python instructions in python3 console: 
    ```python
    import hello_ext
    hello_ext.great()
    ```

And finally you're good!