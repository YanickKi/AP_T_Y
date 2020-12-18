all: build/main.pdf

# hier Python-Skripte:
build/uct.pdf: datascripts/uct.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python datascripts/uct.py

build/volfreq.pdf: datascripts/volfreq.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python datascripts/volfreq.py

build/phasefreq.pdf: datascripts/phasfreq.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python datascripts/phasfreq.py

build/polar.pdf: datascripts/polar.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python datascripts/polar.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/uct.pdf build/volfreq.pdf build/phasefreq.pdf build/polar.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
