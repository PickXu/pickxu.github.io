WEB_DEST=linux.cs.uchicago.edu:/stage/classes/archive/2016/winter/23200-1/

.PHONY:
all: freeze
	
.PHONY: 
clean:
	rm -Rf build/
	
.PHONY:
freeze: clean
	mkdir build
	python freeze.py
	
.PHONY:
upload: freeze
	rsync -a build/ $(WEB_DEST)
	
	