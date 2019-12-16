.PHONY: all
all: docs

.PHONY: clean
clean:
	rm -rf Documentation/*.txt


docs:
	jupyter-nbconvert --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=600 --execute --inplace README.ipynb
	jupyter-nbconvert --to markdown --output=README.md README.ipynb

