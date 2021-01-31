all: build/main.pdf


build/vana.pdf: data_scripts/vana.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/vana.py

build/rho.pdf: data_scripts/rho.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/rho.py

build/rhoall.pdf: data_scripts/rhoall.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/rhoall.py

build/main.pdf: build/rho.pdf build/vana.pdf build/rhoall.pdf

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
