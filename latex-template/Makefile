all: build/main.pdf

build/Verdampfungswaerme.pdf: Verdampfungswaerme.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Verdampfungswaerme.py
# hier Python-Skripte:
build/temperatur.pdf: temperatur.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python temperatur.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/temperatur.pdf build/Verdampfungswaerme.pdf

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
