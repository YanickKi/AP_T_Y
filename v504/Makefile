all: build/main.pdf

# hier Python-Skripte:
build/charcurve.pdf: data_scripts/charcurve.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/charcurve.py

build/exponent.pdf: data_scripts/exponent.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/exponent.py

build/startcurr.pdf: data_scripts/startcurr.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/startcurr.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/charcurve.pdf build/exponent.pdf build/startcurr.pdf



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
