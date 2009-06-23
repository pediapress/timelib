all:: timelib.c
	python setup.py build

clean::
	rm -rf *.so build/ dist/

sdist:: timelib.c
	python setup.py build sdist

%.c: %.pyx
	cython $< -o $@
