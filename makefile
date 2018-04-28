show:
	ls build/lib --color=auto -l

dist:
	python setup.py sdist bdist_wheel --universal

upload:
	twine upload dist/*
