all:: timelib.c
	python setup.py build

clean::
	rm -rf *.so build/ dist/

%.c: %.pyx
	cython $< -o $@
