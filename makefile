export PYTHONPATH=$(shell pwd)

default:
	./go.py
clean:
	rm -rf run/
