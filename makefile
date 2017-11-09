export PYTHONPATH=$(shell pwd)

snake:
	snakemake -s foo.snake
default:
	./go.py
clean:
	rm -rf run/
