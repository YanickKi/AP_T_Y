all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py


build/tiefdruck.pdf: data_scripts/tiefdruck.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/tiefdruck.py

build/hochdruck.pdf: data_scripts/hochdruck.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/hochdruck.py

build/zeitabhaengigkeit.pdf: data_scripts/zeitabhaengigkeit.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/zeitabhaengigkeit.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/tiefdruck.pdf build/hochdruck.pdf build/zeitabhaengigkeit.pdf

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