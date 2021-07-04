all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

build/frankherz1.pdf: data_scripts/frankherz1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/frankherz1.py


build/frankherz2.pdf: data_scripts/frankherz2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/frankherz2.py

build/potentialroom.pdf: data_scripts/potentialroom.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/potentialroom.py

build/potentialhot.pdf: data_scripts/potentialhot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/potentialhot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/frankherz1.pdf build/frankherz2.pdf build/potentialroom.pdf build/potentialhot.pdf

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
