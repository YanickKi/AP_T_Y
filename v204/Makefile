all: build/main.pdf

# hier Python-Skripte:
build/dynamisch40.pdf: data_scripts/dynamisch40.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/dynamisch40.py

build/dynamisch200.pdf: data_scripts/dynamisch200.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/dynamisch200.py

build/stat14.pdf: data_scripts/stat14.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/stat14.py

build/stat58.pdf: data_scripts/stat58.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/stat58.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/stat14.pdf build/stat58.pdf build/dynamisch200.pdf build/dynamisch40.pdf

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
