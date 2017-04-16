# Generate rst documents with raw source from Ulysses

all:
	python transform.py
	pandoc --from markdown --to rst source.md -o source.rst --wrap=preserve
	python split.py