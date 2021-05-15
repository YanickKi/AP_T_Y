all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

build/big.pdf: data_scripts/big.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/big.py


build/middle.pdf: data_scripts/middle.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/middle.py

build/tiny.pdf: data_scripts/tiny.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/tiny.py	

build/velocity.pdf: data_scripts/velocity.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/velocity.py

build/intensitiy.pdf: data_scripts/intensitiy.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/intensitiy.py			
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/big.pdf build/middle.pdf build/tiny.pdf build/velocity.pdf build/intensitiy.pdf
 
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
